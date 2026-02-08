import pytest
from src.utils.exceptions import ValidationError
from src.validators.customer_validator import CustomerValidator

def test_validar_email_ok():
    assert CustomerValidator.validate_email("Juan.Test+1@Mail.com") == "juan.test+1@mail.com"

@pytest.mark.parametrize("email", ["", "a@", "a@b", "a@b.", "a@.com", None])
def test_validar_email_malo(email):
    with pytest.raises(ValidationError):
        CustomerValidator.validate_email(email)

def test_validar_telefono_ok():
    assert CustomerValidator.validate_phone("12 345-678") == "12345678"
    assert CustomerValidator.validate_phone("+56 9 1234-5678").startswith("+")

@pytest.mark.parametrize("tel", ["abc", "123", "+-123", None])
def test_validar_telefono_malo(tel):
    with pytest.raises(ValidationError):
        CustomerValidator.validate_phone(tel)

def test_validar_direccion_ok():
    assert CustomerValidator.validate_address("Av. Siempre Viva 123") == "Av. Siempre Viva 123"

@pytest.mark.parametrize("dir_", ["", "   ", "abc", None])
def test_validar_direccion_mala(dir_):
    with pytest.raises(ValidationError):
        CustomerValidator.validate_address(dir_)

@pytest.mark.parametrize("val, esperado", [(1, 1), ("2", 2), (" 3 ", 3)])
def test_validar_id_ok(val, esperado):
    assert CustomerValidator.validate_customer_id(val) == esperado

@pytest.mark.parametrize("val", [0, -1, "0", "abc", None, True])
def test_validar_id_malo(val):
    with pytest.raises(ValidationError):
        CustomerValidator.validate_customer_id(val)
