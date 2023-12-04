FROM python:3.8.12-slim

RUN pip install pipenv
RUN pip install numpy

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["gateway.py", "proto.py", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen", "0.0.0.0:9696", "gateway:app"]