import allure
from base_api import login_courier
from helpers import create_login_data, generate_courier


class TestLoginCourier:
    @allure.title('Успешная авторизация курьера')
    @allure.description('Проверка, что курьер может авторизоваться и успешный запрос возвращает id')
    def test_login_courier_success(self, registered_courier):
        payload = registered_courier
        response = login_courier(payload)
        assert response.status_code == 200
        assert 'id' in response.json()


    @allure.title('Авторизация курьера без логина')
    @allure.description('Проверка, что система вернет ошибку, если не указать логин при авторизации')
    def test_login_courier_no_login(self, registered_courier):
        courier_data = create_login_data(registered_courier)
        courier_data['login'] = ''
        response = login_courier(courier_data)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'


    @allure.title('Авторизация курьера без пароля')
    @allure.description('Проверка, что система вернет ошибку, если не указать пароль при авторизации')
    def test_login_courier_no_password(self, registered_courier):
        courier_data = create_login_data(registered_courier)
        courier_data['password'] = ''
        response = login_courier(courier_data)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'


    @allure.title('Авторизация с неверным логином')
    @allure.description('Проверка, что система вернет ошибку, если неправильно указать логин при авторизации')
    def test_login_courier_invalid_login(self, registered_courier):
        courier_data = create_login_data(registered_courier)
        new_courier_data = generate_courier()
        courier_data['login'] = new_courier_data['login']
        response = login_courier(courier_data)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'


    @allure.title('Авторизация с неверным паролем')
    @allure.description('Проверка, что система вернет ошибку, если неправильно указать пароль при авторизации')
    def test_login_courier_invalid_password(self, registered_courier):
        courier_data = create_login_data(registered_courier)
        new_courier_data = generate_courier()
        courier_data['password'] = new_courier_data['password']
        response = login_courier(courier_data)
        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'
