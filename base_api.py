import requests
from data import create_courier_url, login_courier_url, delete_courier_url, create_order_url


# Регистрирация курьера
def create_courier(payload):
    return requests.post(create_courier_url, json=payload)
# Авторизация курьера
def login_courier(payload):
    return requests.post(login_courier_url, json=payload)
# Удаление курьера по ID
def delete_courier_by_id(id_courier):
    return requests.delete(f'{delete_courier_url}/{id_courier}')
# Удаление курьера, предварительно авторизуясь для получения ID курьера
def delete_courier(payload):
    response = login_courier(payload)
    id_courier = response.json()['id']
    delete_courier_by_id(id_courier)


# Создание нового заказа
def create_order(payload):
    return requests.post(create_order_url, json=payload)
# Возвращание списка всех заказов
def get_orders_list():
    return requests.get(create_order_url)
