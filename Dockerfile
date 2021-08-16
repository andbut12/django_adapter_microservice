FROM python:3.7.9-slim-buster

RUN mkdir -p /usr/share/man/man1; mkdir -p /home/example/project; mkdir /home/example/logs; \
    pip install --upgrade pip; \
    apt-get update; \
    apt-get -y install gcc git python3-wheel build-essential \
    default-mysql-client libmariadbclient-dev default-libmysqlclient-dev; \
    rm -rf /var/lib/apt/lists/*

ADD . /home/example/project
WORKDIR /home/example/project/
RUN pip install -r requirements.txt
