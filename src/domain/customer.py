from src.utils.exceptions import RequiredFieldError
from src.validators.customer_validators import (
    validate_customer_id,
    validate_required_string,
    validate_email,
    validate_phone,
    validate_address,
)


class Customer:
    REQUIRED_FIELDS = ["customer_id", "name", "email", "phone", "address"]

    def __init__(self, **kwargs):
        missing = [f for f in self.REQUIRED_FIELDS if kwargs.get(f) is None]
        if missing:
            raise RequiredFieldError(f"Faltan campos obligatorios: {', '.join(missing)}")

        self.customer_id = validate_customer_id(kwargs.get("customer_id"))
        self.name = validate_required_string(kwargs.get("name"), "name", min_len=1)

        self.email = kwargs.get("email")
        self.phone = kwargs.get("phone")
        self.address = kwargs.get("address")

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._email = validate_email(value)

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str) -> None:
        self._phone = validate_phone(value)

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str) -> None:
        self._address = validate_address(value)

    def __str__(self) -> str:
        return f"Customer(customer_id={self.customer_id}, name='{self.name}', email='{self.email}')"

    def __eq__(self, other) -> bool:
        return isinstance(other, Customer) and self.customer_id == other.customer_id
