FROM python:3.10-alpine

COPY requirements.txt /temp/requirements.txt

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password testuser
WORKDIR converter
COPY . .
EXPOSE 8000
USER testuser
