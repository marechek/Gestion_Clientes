from src.persistence.customer_json_storage import CustomerJsonStorage
from src.services.customer_mapper import CustomerMapper
from src.utils.exceptions import ValidationError


class CustomerService:
    def __init__(self, storage: CustomerJsonStorage):
        self.storage = storage

    def _normalize_customer_type(self, raw_value: str) -> str:
        if raw_value is None:
            raise ValidationError("Tipo de cliente inválido.")

        value = raw_value.strip().lower()

        mapping = {
            "1": "regular",
            "regular": "regular",
            "2": "premium",
            "premium": "premium",
            "3": "corporate",
            "corporate": "corporate",
        }

        customer_type = mapping.get(value)
        if not customer_type:
            raise ValidationError("Tipo de cliente inválido. Use 1/2/3 o regular/premium/corporate.")
        return customer_type

    def _normalize_customer_id(self, raw_value: str) -> int:
        if raw_value is None:
            raise ValidationError("ID inválido.")
        value = raw_value.strip()
        if not value.isdigit():
            raise ValidationError("ID inválido. Debe ser un número.")
        customer_id = int(value)
        if customer_id <= 0:
            raise ValidationError("ID inválido. Debe ser mayor a 0.")
        return customer_id
    
    def _find_index_by_id(self, customers_list: list, customer_id: int):
        if not isinstance(customer_id, int) or customer_id <= 0:
            raise ValidationError("ID inválido.")

        for i, c in enumerate(customers_list):
            if c.get("customer_id") == customer_id:
                return i
        return None

    def get_customer_by_id_from_input(self, raw_customer_id: str):
        customer_id = self._normalize_customer_id(raw_customer_id)
        return self.get_customer_by_id(customer_id)

    def exists_customer_from_input(self, raw_customer_id: str) -> bool:
        customer = self.get_customer_by_id_from_input(raw_customer_id)
        return customer is not None

    def create_customer_from_input(self, raw_customer_type: str, name: str, email: str, phone: str, address: str):
        customer_type = self._normalize_customer_type(raw_customer_type)
        return self.create_customer(
            customer_type=customer_type,
            name=name,
            email=email,
            phone=phone,
            address=address
        )

    def update_customer_from_input(self, raw_customer_id: str, raw_customer_type: str | None = None, **changes):
        customer_id = self._normalize_customer_id(raw_customer_id)

        if raw_customer_type is not None:
            changes["customer_type"] = self._normalize_customer_type(raw_customer_type)

        return self.update_customer(customer_id, **changes)

    def delete_customer_from_input(self, raw_customer_id: str) -> bool:
        customer_id = self._normalize_customer_id(raw_customer_id)
        return self.delete_customer(customer_id)

    # Operaciones con clientes
    def list_customers(self) -> list:
        data = self.storage.load()
        return [CustomerMapper.from_dict(c) for c in data["customers"]]

    def get_customer_by_id(self, customer_id: int):
        data = self.storage.load()
        for c in data["customers"]:
            if c.get("customer_id") == customer_id:
                return CustomerMapper.from_dict(c)
        return None

    def print_console_report(self) -> None:
        clientes = self.list_customers()

        if not clientes:
            print("\nNo hay clientes registrados.\n")
            return

        widths = {
            "id": 6,
            "name": 20,
            "phone": 15,
            "email": 30,
            "address": 30,
            "benefits": 45,
        }

        def _truncate(text: str, max_len: int) -> str:
            text = "" if text is None else str(text)
            return text if len(text) <= max_len else text[: max_len - 3] + "..."

        total_width = sum(widths.values()) + 5

        print("\n" + "=" * total_width)
        print("LISTADO DE CLIENTES".center(total_width))
        print("=" * total_width)

        print(
            f"{'ID':<{widths['id']}} "
            f"{'Nombre':<{widths['name']}} "
            f"{'Teléfono':<{widths['phone']}} "
            f"{'Email':<{widths['email']}} "
            f"{'Dirección':<{widths['address']}} "
            f"{'Beneficios':<{widths['benefits']}}"
        )

        print("-" * total_width)

        for c in clientes:
            print(
                f"{_truncate(c.customer_id, widths['id']):<{widths['id']}} "
                f"{_truncate(c.name, widths['name']):<{widths['name']}} "
                f"{_truncate(c.phone, widths['phone']):<{widths['phone']}} "
                f"{_truncate(c.email, widths['email']):<{widths['email']}} "
                f"{_truncate(c.address, widths['address']):<{widths['address']}} "
                f"{_truncate(c.get_benefits(), widths['benefits']):<{widths['benefits']}}"
            )

        print("=" * total_width + "\n")

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

        customer_obj = CustomerMapper.from_dict(raw)
        data["customers"].append(CustomerMapper.to_dict(customer_obj))
        self.storage.save(data)
        return customer_obj

    def update_customer(self, customer_id: int, **changes):
        data = self.storage.load()
        idx = self._find_index_by_id(data["customers"], customer_id)
        if idx is None:
            return None

        current = data["customers"][idx]

        allowed = {"name", "email", "phone", "address", "customer_type"}
        for k, v in changes.items():
            if k in allowed and v is not None:
                current[k] = v

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
