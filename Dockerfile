FROM python:3.10.7

ENV PYTHONUNBUFFERED 1
ENV HOST_URL host.docker.internal

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000

