from __future__ import annotations

from typing import Any, Dict

from src.domain.customer import Customer


class CustomerMapper:
    @staticmethod
    def to_dict(customer: Customer) -> Dict[str, Any]:
        return {
            "customer_id": customer.customer_id,
            "customer_type": getattr(customer, "customer_type", "regular"),
            "name": customer.name,
            "email": customer.email,
            "phone": customer.phone,
            "address": customer.address,
            "active": getattr(customer, "active", True),
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> Customer:
        return Customer(
            customer_id=data.get("customer_id"),
            customer_type=data.get("customer_type", "regular"),
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            address=data.get("address"),
            active=data.get("active", True),
        )


