import re
from src.utils.exceptions import ValidationError

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")


def validate_required_string(value: str, field: str, min_len: int = 1) -> str:
    if value is None:
        raise ValidationError(f"El campo '{field}' es obligatorio.")
    if not isinstance(value, str):
        raise ValidationError(f"El campo '{field}' debe ser texto.")
    cleaned = value.strip()
    if len(cleaned) < min_len:
        raise ValidationError(f"El campo '{field}' debe tener al menos {min_len} caracteres.")
    return cleaned


def validate_email(email: str) -> str:
    email = validate_required_string(email, "email", min_len=5).lower()
    if not EMAIL_RE.match(email):
        raise ValidationError("Email inválido.")
    return email


def validate_phone(phone: str) -> str:
    phone = validate_required_string(phone, "phone", min_len=8)
    normalized = phone.replace(" ", "").replace("-", "")

    # Permite + al inicio
    digits = normalized[1:] if normalized.startswith("+") else normalized

    if not digits.isdigit():
        raise ValidationError("Teléfono inválido (solo números o '+' al inicio).")
    if not (8 <= len(digits) <= 15):
        raise ValidationError("Teléfono inválido (largo fuera de rango).")

    return normalized


def validate_address(address: str) -> str:
    return validate_required_string(address, "address", min_len=5)


def validate_customer_id(customer_id) -> int:
    if customer_id is None:
        raise ValidationError("El campo 'customer_id' es obligatorio.")
    if isinstance(customer_id, bool):
        raise ValidationError("ID inválido.")
    if isinstance(customer_id, int):
        if customer_id <= 0:
            raise ValidationError("El ID debe ser mayor a 0.")
        return customer_id
    if isinstance(customer_id, str) and customer_id.strip().isdigit():
        val = int(customer_id.strip())
        if val <= 0:
            raise ValidationError("El ID debe ser mayor a 0.")
        return val
    raise ValidationError("ID inválido.")
