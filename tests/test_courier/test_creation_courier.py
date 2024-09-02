import requests
import helpers
import allure
from data import Url


class TestsCreationCourier:

    @allure.title('Проверка возможности создания курьера. Заполнены все обязательные поля.'
                  'Ручка /api/v1/courier')
    def test_creation_courier_basic_true(self, creation_courier):
        code_response = creation_courier[1]
        body_response = creation_courier[2]
        assert code_response == 201 and (
            body_response == {'ok': True}
        ), (
            f'Status code is {code_response}, body={body_response}'
        )

    @allure.title('Проверка невозможности создания двух одинаковых курьеров. Логин, пароль и имя идентичны.'
                  'Ручка /api/v1/courier')
    def test_creation_two_full_identical_couriers_error(self, creation_courier):
        response = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATION_COURIER}', json=creation_courier[0])
        assert response.status_code == 409 and (
                response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
        ), (
            f'Status code is {response.status_code}, body={response.json()}'
        )
        print(response.status_code)
        print(response.json())

    @allure.title('Проверка невозможности создания курьера. Не заполнено поле "password".'
                  'Ручка /api/v1/courier')
    def test_creation_courier_incomplete_data_error(self):
        data_courier = {'login': helpers.generation_login(), 'first_name': helpers.generation_first_name()}
        response = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATION_COURIER}', json=data_courier)
        assert response.status_code == 400 and (
                response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
        ), (
            f'Status code is {response.status_code}, body={response.json()}'
        )
        print(response.status_code)
        print(response.json())
