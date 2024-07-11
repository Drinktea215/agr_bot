FROM python:3.12

COPY requirements.txt requirements.txt

COPY sampleDB sampleDB

COPY .env .env

COPY agregator.py agregator.py

COPY config.py config.py

COPY main.py main.py

COPY mongo_client.py mongo_client.py

COPY schemas.py schemas.py

WORKDIR .

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install -r requirements.txt