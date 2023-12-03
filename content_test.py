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

    response_data = sentiment_response.json()

    # extracting information from json response
    actual_score = response_data.get('score', None)
    response_username = response_data.get('username', None)
    response_version = response_data.get('version', None)
    response_sentence = response_data.get('sentence', None)

    # POSITIVE if >=0 else NEGATIVE
    if actual_score is not None:
        test_status_sentiment = 'POSITIVE' if actual_score >= 0 else 'NEGATIVE'
    else:
        test_status_sentiment = 'UNKNOWN' # bob v2 will version and status will be unknown

    sentiment_output = f'''
    ===========================================================
        Sentiment Analysis Test: Content test => SCORE TEST
    ===========================================================

    request done at "/{api_version}/sentiment"
    | username="{response_username}"
    | version="{response_version}"
    | sentence="{response_sentence}"

    actual score = {actual_score}
    Classification = {test_status_sentiment}

    '''

    print(sentiment_output)

    if os.environ.get('LOG') == '1':
        with open(log_path, 'a') as file:
            file.write(sentiment_output)

wait_for_service(f'http://{api_address}:{api_port}', "status", expected_response="1")

users = [('alice', 'wonderland'), ('bob', 'builder')]
sentences = ['life is beautiful', 'that sucks']

for user in users:
    for sentence in sentences:
        perform_sentiment_analysis_test(user[0], user[1], sentence, 'v1')
        perform_sentiment_analysis_test(user[0], user[1], sentence, 'v2')
