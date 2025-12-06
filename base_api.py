import requests
from data import Urls


class Api:
    # Регистрирует курьера через POST-запрос
    def register_user(payload):
        return requests.post(create_courier, json=payload)
    # Логинит курьера через POST-запрос
    def login_user(payload):
        return requests.post(login_courier, json=payload)
    # Удаляет курьера по ID через DELETE-запрос
    def delete_user_by_id(id_user):
        return requests.delete(f"{create_courier}/{id_user}")
    # Удаляет курьера, сначала логинясь для получения ID
    def delete_user(payload):
        response = login_user(payload)
        id_user = response.json()["id"]
        delete_user_by_id(id_user)



    def create_order(payload):
        """Создает новый заказ через POST-запрос."""
        return requests.post(ORDERS_URL, json=payload)

    def cancel_order(track):
        """Отменяет заказ по его трек-номеру через PUT-запрос."""
        return requests.put(ORDERS_CANCEL_URL, json={"track": track})

    def get_list_orders():
        """Возвращает список всех заказов через GET-запрос."""
        return requests.get(ORDERS_URL)    