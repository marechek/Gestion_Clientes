import pytest
from src.domain.customer import Customer
from src.utils.exceptions import ValidationError, RequiredFieldError


def test_create_valid_customer():
    customer = Customer(
        customer_id=1,
        name="Juan Perez",
        email="JUAN@test.com",
        phone="12 345-678",
        address="Av. Siempre Viva 123"
    )
    assert customer.email == "juan@test.com"
    assert customer.phone == "12345678"


def test_missing_required_fields():
    with pytest.raises(RequiredFieldError):
        Customer(customer_id=1, name="Juan", email="a@a.com", phone="12345678")


def test_invalid_email():
    with pytest.raises(ValidationError):
        Customer(
            customer_id=2,
            name="Test",
            email="email_invalido",
            phone="12345678",
            address="Direccion valida"
        )


def test_eq_customers():
    c1 = Customer(customer_id=1, name="A", email="a@test.com", phone="12345678", address="Dir 1")
    c2 = Customer(customer_id=1, name="B", email="b@test.com", phone="87654321", address="Dir 2")
    assert c1 == c2


