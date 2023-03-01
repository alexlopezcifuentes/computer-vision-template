FROM pytorch/pytorch:latest

WORKDIR /app
ADD . /app

RUN apt-get update -y
RUN pip install --upgrade pip
RUN pip install -r docker-dev/requirements.txt
