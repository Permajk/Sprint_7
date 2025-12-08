import allure
from base_api import get_orders_list


class TestOrderList:
    @allure.title('Получение списка заказов')
    @allure.description('Проверка, что в тело ответа возвращается список заказов')
    def test_orders_list_success(self):
        response = get_orders_list()
        assert response.status_code == 200
        assert "orders" in response.json()
