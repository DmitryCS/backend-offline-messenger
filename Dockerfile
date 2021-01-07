FROM ubuntu:20.04
MAINTAINER Dmitry Lyzhin 'dmitry.lyzhin2014@yandex.ru'
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
COPY . /backend-offline-messenger
WORKDIR /backend-offline-messenger
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["main.py"]