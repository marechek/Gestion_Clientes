from src.persistence.customer_json_storage import CustomerJsonStorage
from src.services.customer_mapper import CustomerMapper
from src.utils.exceptions import ValidationError


class CustomerService:
    def __init__(self, storage: CustomerJsonStorage):
        self.storage = storage

    def list_customers(self) -> list:
        data = self.storage.load()
        return [CustomerMapper.from_dict(c) for c in data["customers"]]

    def get_customer_by_id(self, customer_id: int):
        data = self.storage.load()
        for c in data["customers"]:
            if c.get("customer_id") == customer_id:
                return CustomerMapper.from_dict(c)
        return None

    def create_customer(self, customer_type: str, name: str, email: str, phone: str, address: str):
        data = self.storage.load()

        # Autoincremental
        data["last_id"] = int(data.get("last_id", 0)) + 1
        new_id = data["last_id"]

        raw = {
            "customer_id": new_id,
            "name": name,
            "email": email,
            "phone": phone,
            "address": address,
            "customer_type": (customer_type or "regular").lower(),
        }

        customer_obj = CustomerMapper.from_dict(raw)  # valida y crea la subclase
        data["customers"].append(CustomerMapper.to_dict(customer_obj))
        self.storage.save(data)
        return customer_obj

    def update_customer(self, customer_id: int, **changes):
        data = self.storage.load()
        idx = self._find_index_by_id(data["customers"], customer_id)
        if idx is None:
            return None

        current = data["customers"][idx]

        # Solo permitimos actualizar estos campos
        allowed = {"name", "email", "phone", "address", "customer_type"}
        for k, v in changes.items():
            if k in allowed and v is not None:
                current[k] = v

        # Revalida reconstruyendo objeto
        updated_obj = CustomerMapper.from_dict(current)
        data["customers"][idx] = CustomerMapper.to_dict(updated_obj)
        self.storage.save(data)
        return updated_obj

    def delete_customer(self, customer_id: int) -> bool:
        data = self.storage.load()
        idx = self._find_index_by_id(data["customers"], customer_id)
        if idx is None:
            return False

        data["customers"].pop(idx)
        self.storage.save(data)
        return True

    def _find_index_by_id(self, customers_list: list, customer_id: int):
        if not isinstance(customer_id, int) or customer_id <= 0:
            raise ValidationError("ID inválido.")

        for i, c in enumerate(customers_list):
            if c.get("customer_id") == customer_id:
                return i
        return None

