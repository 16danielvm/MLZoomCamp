FROM python:3.10-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "model_C=1.0.bin", "./"]

ENTRYPOINT ["waitress-serve", "--listen", "0.0.0.0:9696", "predict:app"]