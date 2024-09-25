FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apt-get update -y && apt-get -y install gcc
RUN pip install -r requirements.txt

COPY . /app/
RUN python main.py
