FROM python:3.4

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt

ADD . /code/

CMD python manage.py makemigrations
CMD python manage.py migrate

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash
RUN apt-get install --yes nodejs

RUN npm install gulp
RUN npm install
