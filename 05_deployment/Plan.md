## 5.1 Intro / Session overview

* What we will cover this week

## 5.2. Saving and loading the model

* Saving the model to pickle

* Loading the model from pickle

* Turning the notebook into a Python script
    * Create train.py
    * Create predict.py

## 5.3. Web services: Introduction to Flask

* Writing a simple ping/pong app
* Querying it with 'curl' and browser (just browser)

## 5.4. Serving the churn model with Flask

* Wrapping the predict script into a Flask app
    * Change predict.py creating a Flask app
        * Method POST
        * Getting the customer as a json with flask.request with request.get_json()
        * Jsonifying the result

* Querying it with 'request'
    * Create the predict_test.py
        * Url = localhost:9696/predict
        * Customer as json '' -> ""
        * Use library requests.post to send the customer data

* Preparing for production: gunicorn 

* Running it on Windows with waitress
    * waitress-serve --listen 0.0.0.0:9696 predict:app

## 5.5. Dependency and enviroment management: Pipenv

* Why we need virtual enviroment

* Installing Pipenv
    * pip install pipenv

* Installing libreries with Pipenv
    * 'pipenv' install -libraries- (instead of 'pip') -> this create a virtual environment
        * A pipfile and pipfile.lock are automatically created
            * Pipfile has the requierements (packages, versions, etc).
            * Pipfile.lock is a big json file which has the versions of all dependencies.

* Running things with Pipenv
    * pipenv shell to activate - exit to deasactivate the pipenv
        * pipenv --rm to eliminate the venv
    * waitress-serve --listen 0.0.0.0:9696 predict:app


## 5.6. Environment management: Docker
* Why we need Docker
* Running a Python image with docker
* Dockerfile
* Building a docker image