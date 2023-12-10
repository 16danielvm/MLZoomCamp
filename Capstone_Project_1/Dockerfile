FROM public.ecr.aws/lambda/python:3.10

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --system --deploy

COPY ["final_model.bin", "./"]
COPY lambda_function.py .

CMD [ "lambda_function.lambda_handler" ]

