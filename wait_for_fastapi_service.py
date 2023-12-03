import requests
import time

# function that verifies the healthcheck of the api: in this case: localhost:8000/status that returns 1 if api is working fine.
# 30 retries in case it needs some time
def wait_for_service(service_url, health_check_path, expected_response="1", max_retries=30):
    url = f"{service_url}/{health_check_path}"
    retries = 0

    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            if response.text.strip() == expected_response:
                print(f"Service at {service_url} is ready!")
                return
            else:
                print(f"Service at {service_url} returned unexpected response: {response.text.strip()}")
        except requests.exceptions.RequestException as e:
            print(f"Waiting for service at {service_url}: {e}")
        retries += 1
        time.sleep(1)

    raise Exception(f"Service at {service_url} was not ready within the timeout period")
