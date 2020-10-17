FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code
ADD requirements.txt /code/

RUN pip3 install -r requirements.txt
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install sklearn
RUN pip3 install janome
RUN pip3 install django-picklefield
RUN pip3 install psycopg2
RUN pip3 install dj-database-url
RUN pip3 install whitenoise==5.0.1
RUN pip3 install gunicorn
RUN pip3 install pytz
RUN pip3 install django-heroku
RUN apt-get update && apt-get -y install vim
ADD . /code/

EXPOSE 8000
