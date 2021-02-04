import os
import uuid

from sanic import response
from sanic.request import Request
from sanic.response import BaseHTTPResponse

from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBFileNotExistsException
from transport.sanic.endpoints import BaseEndpoint
from db.queries import file as file_queries
from transport.sanic.exceptions import SanicDBException, SanicFileNotFound, SanicUserConflictException


class FilesEndpoint(BaseEndpoint):

    async def method_get(
            self, request: Request, body: dict, session: DBSession, file_id: int = None, *args, **kwargs
    ) -> BaseHTTPResponse:
        try:
            file = file_queries.get_file_by_id(session, file_id=file_id)
        except DBFileNotExistsException:
            raise SanicFileNotFound('File not found')
        if file.sender_id != body['uid']:
            if body['uid'] not in file_queries.get_recipients_by_file_id(session, file_id):
                raise SanicUserConflictException("You don't have access to the file")

        return await response.file(os.path.join('raw_files', file.ref_file), status=200)

    async def method_post(
            self, request: Request, body: dict, session: DBSession, *args, **kwargs
    ) -> BaseHTTPResponse:
        if not os.path.exists('raw_files'):
            os.makedirs('raw_files')
        files = request.files['file']
        file_names = []
        for f in files:
            filename = '.'.join([str(uuid.uuid4()), f.name.split('.')[-1]])
            path_to_file = os.path.join('raw_files', filename)
            with open(path_to_file, 'wb') as file:
                file.write(f.body)
            file_names.append(filename)
        files = []
        for f_name in file_names:
            file = file_queries.create_file(session, body['uid'], f_name)
            files.append(file)
        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))
        file_ids = []
        for file in files:
            file_ids.append(file.id)

        return await self.make_response_json(body={"file_ids": file_ids}, status=201)
