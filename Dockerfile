FROM python:3
EXPOSE 8000

RUN git clone https://github.com/DmitryCS/backend-offline-messenger.git
RUN pip install --no-cache-dir -r /backend-offline-messenger/requirements.txt