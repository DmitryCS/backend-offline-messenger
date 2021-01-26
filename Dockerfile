FROM python:3
EXPOSE 8000

RUN git clone https://github.com/DmitryCS/tasks.git
RUN pip install --no-cache-dir -r /tasks/requirements.txt