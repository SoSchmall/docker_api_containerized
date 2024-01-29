## Overview
This project centers around a FastAPI application designed for sentiment analysis. The application predicts whether a given English sentence has a positive or negative sentiment. It is deployed in a Docker container, currently using the image datascientest/fastapi:1.0.0. The application offers several endpoints:

* /status: Returns 1 if the API is operational.
* /permissions: Provides the permissions of a user.
* /v1/sentiment: Performs sentiment analysis using an older model.
* /v2/sentiment: Conducts sentiment analysis using a newer, more advanced model.

## What is being tested

* Operational Status: Verifying the API's operational status through the /status endpoint.
* Authentication and Permissions: Testing the /permissions endpoint to ensure accurate representation of user permissions.
* Sentiment Analysis - Version 1: Assessing the performance and accuracy of the older sentiment analysis model provided by the /v1/sentiment endpoint.
* Sentiment Analysis - Version 2: Evaluating the newer sentiment analysis model available through the /v2/sentiment endpoint, comparing its effectiveness to the older version.

## Building the project 

_The following script builds the application and tests the endpoints in isolated Docker environments_
```sh
./setup
```
## Healthcheck implementation

For each test, I include the file wait_for_fastapi_service.py, which checks
the status of the application that should returns 1 (checking healthcheck) before
running the tests. 

This is done particularly because "depends on" on docker-compose.yml does not make sure
the service is "ready". It ensures only the dependency order. Meaning if service A depends on service B
then service B starts before. But a verification that the service is fully initialized is required.
