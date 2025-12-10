import allure
import pytest
from data import base_order_payload, order_colors
from base_api import create_order 


class TestOrderCreate:
    @allure.title('Создание заказа')
    @allure.description('Проверка, что можно создать заказ с разными вариантами цвета')
    @pytest.mark.parametrize('color', order_colors)
    def test_order_create(self, color):
        with allure.step('Проверка создания копии заказа с параметризацией разных вариантов цветов'):
            payload = base_order_payload(color).copy()
        with allure.step('Проверка создания заказа с разними комбинациями цветов c "track" в теле'):
            response = create_order(payload)
            assert response.status_code == 201
            assert "track" in response.json()
