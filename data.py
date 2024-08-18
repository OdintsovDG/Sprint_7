class Url:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/'
    POST_CREATION_COURIER = 'api/v1/courier'
    POST_LOGIN_COURIER = 'api/v1/courier/login'
    DELETE_COURIER = 'api/v1/courier/'
    POST_CREATION_ORDER = 'api/v1/orders'
    GET_ORDERS_LIST = 'api/v1/orders'
    PUT_ORDER = 'api/v1/orders/cancel'


class DataForOrder:
    data_without_color = {"firstName": "Dmitriy",
                          "lastName": "Odintsov",
                          "address": "Kraulya st. 89A",
                          "metroStation": 4,
                          "phone": "+79008007766",
                          "rentTime": 2,
                          "deliveryDate": "2024-09-01",
                          "comment": "When you finish the delivery, please call me"
                          }
    color_for_scooter = [['BLACK'], ['GREY'], (['BLACK'], ['GREY']), ['']]
