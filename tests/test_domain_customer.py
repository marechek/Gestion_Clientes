import pytest
from src.domain.customer import Customer
from src.domain.regular_customer import RegularCustomer
from src.domain.premium_customer import PremiumCustomer
from src.domain.corporate_customer import CorporateCustomer
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


def test_regular_customer_benefits():
    c = RegularCustomer(
        customer_id=1,
        name="Juan",
        email="a@a.com",
        phone="12345678",
        address="Direccion valida"
    )
    assert "regular" in c.get_benefits().lower()


def test_premium_customer_benefits():
    c = PremiumCustomer(
        customer_id=2,
        name="Ana",
        email="b@b.com",
        phone="12345678",
        address="Direccion valida"
    )
    assert "premium" in c.get_benefits().lower()


def test_corporate_customer_benefits():
    c = CorporateCustomer(
        customer_id=3,
        name="Empresa",
        email="c@c.com",
        phone="12345678",
        address="Direccion valida"
    )
    assert "corporativo" in c.get_benefits().lower()


