import requests
import helpers
import allure
from data import Url


class TestLoginCourier:

    @allure.title('Проверка авторизации курьера. Все обязательные поля заполнены корректно.'
                  'Ручка /api/v1/courier/login')
    def test_login_courier_basic_true(self, creation_courier):
        code_response = creation_courier[4]
        id_courier = creation_courier[3]
        assert code_response == 200 and id_courier is not None, (
            f'Status code is {code_response}, id={id_courier}'
        )
        print(code_response)
        print(id_courier)

    @allure.title('Проверка авторизации несуществующего курьера. Все обязательные поля заполнены.'
                  'Ручка /api/v1/courier/login')
    def test_login_fake_courier_error(self):
        data_courier = {'login': helpers.generation_login(), 'password': helpers.generation_password()}
        response = requests.post(f'{Url.MAIN_URL}{Url.POST_LOGIN_COURIER}', json=data_courier)
        assert response.status_code == 404 and (
                response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}
        ), (
            f'Status code is {response.status_code}, body={response.json()}'
        )
        print(response.status_code)
        print(response.json())

    @allure.title('Проверка авторизации курьера. Заполнено только поле "login".'
                  'Ручка /api/v1/courier/login')
    def test_login_courier_incomplete_data_error(self, creation_courier):
        response = requests.post(f'{Url.MAIN_URL}{Url.POST_LOGIN_COURIER}', json=creation_courier[5])
        assert response.status_code == 400 and (
                response.json() == {'code': 400, 'message': 'Unexpected token " in JSON at position 0'}
        ), (
            f'Status code is {response.status_code}, body={response.json()}'
        )
        print(response.status_code)
        print(response.json())
