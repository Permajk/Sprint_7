from faker import Faker
fake = Faker(locale='ru_RU')


# Генерируем случайные данные для курьера
def generate_courier():
    login = fake.user_name()
    password = fake.password()
    first_name = fake.name()

    courier_data = {
        'login': login,
        'password': password,
        'name': first_name
        }
    return courier_data


# Создает данные для входа на основе данных курьера
def create_login_data(courier_data):
    return {
        'login': courier_data['login'],
        'password': courier_data['password']
    }
