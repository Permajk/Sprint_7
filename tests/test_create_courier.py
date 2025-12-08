import allure
import pytest
from base_api import create_courier
from helpers import generate_courier


class TestCreateCourier:
    @allure.title('Создание курьера')
    @allure.description('Проверка, что курьера можно создать и возвращается код 201 и {"ok": True}')
    def test_create_courier(self, courier_payload_with_delete):
        payload = courier_payload_with_delete
        response = create_courier(payload)
        assert response.status_code == 201
        assert response.json() == {'ok': True}


    @allure.title('Создание двух одинаковых курьеров')
    @allure.description('Проверка, что нельзя создать курьера с логином, который уже есть')
    def test_create_duplicate_courier(self, registered_courier):
        payload = registered_courier
        response = create_courier(payload)
        assert response.status_code == 409
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'


    @allure.title('Создание курьера с пустым обязательным полем')
    @allure.description('Проверка, что нельзя создать курьера с пустым обязательным полем (логин или пароль)')
    @pytest.mark.parametrize('no_field',['login', 'password'])
    def test_create_courier_with_login_or_password(self, no_field):
        payload = generate_courier()
        payload[no_field] = ''
        response = create_courier(payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'
