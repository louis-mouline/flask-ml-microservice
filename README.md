[![MLOps Flask microservice](https://github.com/louis-mouline/flask-ml-microservice/actions/workflows/flask_app.yml/badge.svg)](https://github.com/louis-mouline/flask-ml-microservice/actions/workflows/flask_app.yml)

# Machine Learning microservice using Flask

The project is part of the specialisation course done on Coursera called: ["Specialisation Building Cloud Computing Solutions at Scale"](https://www.coursera.org/specializations/building-cloud-computing-solutions-at-scale).

The objective of the project is to create a containerized Flask application that is continuously deployed to a Cloud platform. This is the final project of the second class called ["Cloud Virtualization, Containers and APIs"](https://www.coursera.org/learn/cloud-virtualization-containers-api-duke/home/welcome).

This repository contains a Flask application which **predict the price of a used cars** based on the following parameters: *model*, *year*, *transmission*, *mileage*, *fuel type*, *tax*, *mpg*, *engine size*, *manufacter*.

## Assets in the repository

The repository is built in the following way:
* `data` folder contains the persisted model and the dataset extracted from [Kaggle](https://www.kaggle.com/adityadesai13/used-car-dataset-ford-and-mercedes);
* `utils` folder contains utilitary files used to ingest data and predict the price of a used car;
* `test` folder contains all files testing the utilitary functions in the previous folder;
* `application.py` sets-up the Flask application;
* `predict.sh` sents a request to the Flask application;
* `run_docker` sets-up and launch a docker for the application based on the `Dockerfile`.

Here is the structure:
```
flask-ml-microservice
└─── data
|    |  model.zlib
|    |  target_scaler.zlib
|    |  used_vehicles.csv
└─── test
|    |  test_data.py
|    |  test_mllib.py
└─── utils
|    |  data.py
|    |  mllib.py
|   application.py
|   Dockerfile
|   Makefile
|   predict.sh
|   README.md
|   requirements.txt
|   run_docker.sh
|   Used_Car8price_Prediction.ipynb
```

## Flask microservice

The Flask ML Microservice can be run two ways.

### Containerized Flask Microservice Locally

You can run the Flask Microservice as follows with the commmand: `python application.py`.
![launch-app](./docs/flask_local.PNG)

To serve a prediction against the application, run the `predict.sh` or using Postman.
[!postman-flask](./docs/postman-flask.PNG)

### Containerized Flask Microservice

Here is an example of how to build the container and run it locally, this is the contents of `run_docker.sh`.
``` bash
#!/usr/bin/env bash

# Build image
#change tag for new container registery, gcr.io/bob
docker build --tag=flask-mlops . 

# List docker images
docker image ls

# Run flask app
docker run -p 127.0.0.1:8080 flask-mlops
```

## Next steps

- [ ] Add AWS Lambda support
