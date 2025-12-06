
from helpers import Generate
from base_api import Api
import pytest

# Создание и удаление курьера
@pytest.fixture
def courier_payload_with_cleanup():
    payload = generate_courier()
    yield payload
    delete_user(payload)

# Создание, регистрация и удаление курьера
@pytest.fixture
def registered_courier():
    payload = generate_courier()
    register_user(payload)
    yield payload
    delete_user(payload)
