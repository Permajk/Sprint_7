import allure
from base_api import login_courier
from helpers import create_login_data, generate_courier
from data import Авторизация_курьера_без_логина_или_пароля, Авторизация_курьера_с_несуществующим_логином_и_паролем


class TestLoginCourier:
    @allure.title('Успешная авторизация курьера')
    @allure.description('Проверка, что курьер может авторизоваться и успешный запрос возвращает id')
    def test_login_courier_success(self, registered_courier):
        with allure.step('Проверка регистрации курьера через фикстуру'):
            payload = registered_courier
        with allure.step('Проверка авторизации курьера с "id" в теле'):
            response = login_courier(payload)
            assert response.status_code == 200
            assert "id" in response.json()


    @allure.title('Авторизация курьера без логина')
    @allure.description('Проверка, что система вернет ошибку, если не указать логин при авторизации')
    def test_login_courier_no_login(self, registered_courier):
        with allure.step('Проверка создания данные для авторизации на основе данных курьера'):
            courier_data = create_login_data(registered_courier)
        with allure.step('Проверка создания данные для авторизации с пустым логином'):
            courier_data['login'] = ''
        with allure.step('Проверка ошибки авторизации курьера с пустым логином'):
            response = login_courier(courier_data)
            assert response.status_code == 400
            assert response.json()['message'] == Авторизация_курьера_без_логина_или_пароля


    @allure.title('Авторизация курьера без пароля')
    @allure.description('Проверка, что система вернет ошибку, если не указать пароль при авторизации')
    def test_login_courier_no_password(self, registered_courier):
        with allure.step('Проверка создания данные для авторизации на основе данных курьера'):
            courier_data = create_login_data(registered_courier)
        with allure.step('Проверка создания данные для авторизации с пустым паролем'):
            courier_data['password'] = ''
        with allure.step('Проверка ошибки авторизации курьера с пустым паролем'):
            response = login_courier(courier_data)
            assert response.status_code == 400
            assert response.json()['message'] == Авторизация_курьера_без_логина_или_пароля


    @allure.title('Авторизация с неверным логином')
    @allure.description('Проверка, что система вернет ошибку, если неправильно указать логин при авторизации')
    def test_login_courier_invalid_login(self, registered_courier):
        with allure.step('Проверка создания данные для авторизации на основе данных курьера'):
            courier_data = create_login_data(registered_courier)
        with allure.step('Проверка генерации данных другого курьера'):
            new_courier_data = generate_courier()
        with allure.step('Проверка создания другого логина для авторизации'):
            courier_data['login'] = new_courier_data['login']
        with allure.step('Проверка ошибки авторизации курьера с другим логином'):
            response = login_courier(courier_data)
            assert response.status_code == 404
            assert response.json()['message'] == Авторизация_курьера_с_несуществующим_логином_и_паролем


    @allure.title('Авторизация с неверным паролем')
    @allure.description('Проверка, что система вернет ошибку, если неправильно указать пароль при авторизации')
    def test_login_courier_invalid_password(self, registered_courier):
        with allure.step('Проверка создания данные для авторизации на основе данных курьера'):
            courier_data = create_login_data(registered_courier)
        with allure.step('Проверка генерации данных другого курьера'):
            new_courier_data = generate_courier()
        with allure.step('Проверка создания другого пароля для авторизации'):
            courier_data['password'] = new_courier_data['password']
        with allure.step('Проверка ошибки авторизации курьера с другим паролем'):
            response = login_courier(courier_data)
            assert response.status_code == 404
            assert response.json()['message'] == Авторизация_курьера_с_несуществующим_логином_и_паролем
