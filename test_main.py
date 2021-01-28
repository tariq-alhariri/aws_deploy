'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'mySecret'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTMwODEzMzAsIm5iZiI6MTYxMTg3MTczMCwiZW1haWwiOiJ0YXJpcUBtYWlsLmNvbSJ9.WpPy7GoY2gkTe13PfOB4_2ImKdoVh6vvvrQ8WPSwFOI'
EMAIL = 'tariq@mail.com'
PASSWORD = 'password!'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
