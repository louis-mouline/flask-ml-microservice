#!/usr/bin/env bash

# Build image
#change tag for new container registery, gcr.io/bob
docker build --tag=flask-mlops . 

# List docker images
docker image ls

# Run flask app
docker run -p 127.0.0.1:8080 flask-mlops