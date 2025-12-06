from faker import Faker
fake = Faker(locale="ru_RU")


class Generate:

    # Генерируем случайные данные для курьера
    def generate_courier():
        login = fake.user_name()
        password = fake.password()
        first_name = fake.name()

        courier_data = {
            "login": login,
            "password": password,
            "name": first_name
            }
        return courier_data

    # Генерируем случайные данные для курьера без пароля
    def generate_courier_not_password():
        login = fake.user_name()
        first_name = fake.name()

        courier_data = {
            "login": login,
            "password": '',
            "name": first_name
            }
        return courier_data

    # Генерируем случайные данные для курьера без логина
    def generate_courier_not_login():
        password = fake.password()
        first_name = fake.name()

        courier_data = {
            "login": '',
            "password": password,
            "name": first_name
            }
        return courier_data
