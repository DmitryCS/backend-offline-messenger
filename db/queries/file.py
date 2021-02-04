from typing import List

from db.database import DBSession
from db.exceptions import DBFileNotExistsException, DBResourceOwnerException, DBMsgFileNotExistsException
from db.models import DBMsgFile
from db.models.file import DBFile


def create_file(session: DBSession, user_id: int, file_name: str) -> DBFile:
    new_file = DBFile(
        sender_id=user_id,
        ref_file=file_name,
    )

    session.add_model(new_file)

    return new_file


def create_msg_file_relation(session: DBSession, user_id: int, msg_id: int, file_id: int) -> DBMsgFile:
    db_file = session.get_file_by_id(file_id)
    if db_file is None:
        raise DBFileNotExistsException
    if db_file.sender_id != user_id:
        raise DBResourceOwnerException
    msg_file = DBMsgFile(
        msg_id=msg_id,
        file_id=file_id,
    )

    session.add_model(msg_file)

    return msg_file


def delete_msg_file_relation(session: DBSession, user_id: int, msg_id: int, file_id: int) -> None:
    db_msgfile = session.get_msgfile_by_msgfile_ids(msg_id, file_id)
    if db_msgfile is None:
        raise DBMsgFileNotExistsException
    db_file = session.get_file_by_id(file_id)
    if db_file.sender_id != user_id:
        raise DBResourceOwnerException
    db_msgfile.is_delete = True


def get_file_ids_by_msd_id(session: DBSession, msg_id: int) -> List[int]:
    list_file_ids = [file_id.file_id for file_id in session.get_msgfiles_by_msg_id(msg_id)]

    return list_file_ids


def get_file_by_id(session: DBSession, file_id: int) -> DBFile:

    file = session.get_file_by_id(file_id)
    if file is None:
        raise DBFileNotExistsException
    return file


def get_recipients_by_file_id(session: DBSession, file_id: int) -> List[int]:
    msgs_files = session.get_msgfiles_by_file_id(file_id)
    recipient_ids = []
    for msg_file in msgs_files:
        message = session.get_message_by_id(msg_file.msg_id)
        recipient_ids.append(message.recipient_id)
    return recipient_ids
