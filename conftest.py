import pytest
import requests
import helpers
from data import Url


@pytest.fixture
def creation_courier():
    login = helpers.generation_login()  # 5
    password = helpers.generation_password()
    firstName = helpers.generation_first_name()
    data_courier = {'login': login, 'password': password, 'first_name': firstName}  # 0
    authorization = {'login': login, 'password': password}
    crt_courier = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATION_COURIER}', json=data_courier)  # 1,2
    login_courier = requests.post(f'{Url.MAIN_URL}{Url.POST_LOGIN_COURIER}', json=authorization)  # 3,4
    yield (data_courier, crt_courier.status_code, crt_courier.json(),
           login_courier.json()['id'], login_courier.status_code, login)
    requests.delete(f'{Url.MAIN_URL}{Url.DELETE_COURIER}{login_courier.json()['id']}')
