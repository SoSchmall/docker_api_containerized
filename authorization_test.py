import os
import requests
from wait_for_fastapi_service import wait_for_service

api_address = 'fastapi_app'
api_port = 8000
log_path = '/tests_output/api_test.log'

def perform_sentiment_analysis_test(username, password, sentence, api_version):
    sentiment_response = requests.get(
        url=f'http://{api_address}:{api_port}/{api_version}/sentiment',
        params={
            'username': username,
            'password': password,
            'sentence': sentence
        }
    )

    status_code_sentiment = sentiment_response.status_code

    test_status_sentiment = ''

    sentiment_output = f'''
    =================================================== 
        Sentiment Analysis test: Authorization test     
    ===================================================

    request done at "/{api_version}/sentiment"
    | username="{username}"
    | password="{password}"
    | sentence="{sentence}"

    expected result = 200
    actual result = {status_code_sentiment}

    ==>  {test_status_sentiment}

    '''

    if status_code_sentiment == 200:
        test_status_sentiment = 'SUCCESS'
    else:
        test_status_sentiment = 'FAILURE'
    print(sentiment_output.format(status_code=status_code_sentiment, test_status=test_status_sentiment))

    if os.environ.get('LOG') == '1':
        with open(log_path, 'a') as file:
            file.write(sentiment_output)

wait_for_service(f'http://{api_address}:{api_port}', "status", expected_response="1")

# tests
perform_sentiment_analysis_test('alice', 'wonderland', 'Test sentence for v1', 'v1') # success
perform_sentiment_analysis_test('bob', 'builder', 'Test sentence for v1', 'v1') # success
perform_sentiment_analysis_test('clementine', 'mandarine', 'Test sentence for v1', 'v1') # does not exist   

perform_sentiment_analysis_test('alice', 'wonderland', 'Test sentence for v2', 'v2') # success
perform_sentiment_analysis_test('bob', 'builder', 'Test sentence for v2', 'v2') # failure
perform_sentiment_analysis_test('clementine', 'mandarine', 'Test sentence for v2', 'v2') # does not exist
