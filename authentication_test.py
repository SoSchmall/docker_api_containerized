import os
import requests
from wait_for_fastapi_service import wait_for_service

api_address = 'fastapi_app'
api_port = 8000
log_path = '/tests_output/api_test.log'

def perform_authentication_test(username, password):
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params={
            'username': username,
            'password': password
        }
    )

    output_template = '''
    ============================
        Authentication test
    ============================

    request done at "/permissions"
    | username="{username}"
    | password="{password}"

    expected result = 200
    actual result = {status_code}

    ==>  {test_status}

    '''

    status_code = r.status_code

    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output_template.format(username=username, password=password, status_code=status_code, test_status=test_status))

    if os.environ.get('LOG') == '1':
        with open(log_path, 'a') as file:
            file.write(output_template.format(username=username, password=password, status_code=status_code, test_status=test_status))


wait_for_service(f'http://{api_address}:{api_port}', "status", expected_response="1")

# perform status code check for the 3 available users: 200 success/403 forbidden
perform_authentication_test('alice', 'wonderland')
perform_authentication_test('bob', 'builder')
perform_authentication_test('clementine', 'mandarine')
