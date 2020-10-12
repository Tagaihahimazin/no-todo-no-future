FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code
ADD requirements.txt /code/

RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get -y install vim
ADD . /code/

EXPOSE 8000
