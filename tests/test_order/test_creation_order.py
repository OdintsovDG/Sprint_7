import pytest
import requests
import allure
from data import Url, DataForOrder


class TestCreationOrder:

    @allure.title('Проверка создания заказа. Выбор каждого цвета, выбор двух цветов, отсутствие выбора цвета.'
                  'Ручка /api/v1/orders')
    @pytest.mark.parametrize('color_scooter', DataForOrder.color_for_scooter)
    def test_creation_order_choice_color_true(self, color_scooter):
        payload = [DataForOrder.data_without_color, color_scooter]
        order = requests.post(f'{Url.MAIN_URL}{Url.POST_CREATION_ORDER}', json=payload)
        result = 'track'
        assert order.status_code == 201 and result in order.json(), \
            f'status code{order.status_code}, text={order.json()}'
        print(order.status_code)
        print(order.json())
