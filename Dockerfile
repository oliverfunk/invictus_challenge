FROM python:3.6

WORKDIR /service

COPY main.py main.py
COPY conf.yml conf.yml
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

CMD ["nameko", "run", "--config", "conf.yml", "main"]