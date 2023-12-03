Hello!

########################## Running the application  ##########################

You can run setup.sh for building and running the application and the tests:
./setup

########################## Healthcheck implementation  ##########################

For each test, I include the file wait_for_fastapi_service.py, which checks
the status of the application that should returns 1 (checking healthcheck) before
running the tests. 

This is done particularly because "depends on" on docker-compose.yml does not make sure
the service is "ready". It ensures only the dependency order. Meaning if service A depends on service B
then service B starts before. But a verification that the service is fully initialized is required.

########################## LOGS ##########################

Logs can be found under the volume mounted ./volume_for_tests/api_test.log on the host.
Also, it can be found /tests_output inside the containers.
