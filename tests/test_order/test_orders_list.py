import requests
import allure
from data import Url


class TestOrdersList:

    @allure.title('Проверка запроса списка заказов. Ручка /api/v1/orders')
    def test_get_orders_list_in_response_true(self):
        orders_list = requests.get(f'{Url.MAIN_URL}{Url.GET_ORDERS_LIST}')
        result = 'orders'
        assert orders_list.status_code == 200 and result in orders_list.json(), \
            f'status code{orders_list.status_code}, text={orders_list.json()}'
        print(orders_list.status_code)
        print(orders_list.json())
