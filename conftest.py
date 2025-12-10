import pytest
from helpers import generate_courier
from base_api import create_courier, delete_courier


# Создание и удаление курьера
@pytest.fixture
def courier_payload_with_delete():
    payload = generate_courier()
    yield payload
    delete_courier(payload)

# Создание, регистрация и удаление курьера
@pytest.fixture
def registered_courier(courier_payload_with_delete):
    payload = courier_payload_with_delete
    create_courier(payload)
    yield payload
