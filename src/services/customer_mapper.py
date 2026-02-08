from __future__ import annotations

from typing import Any, Dict

from src.domain.customer import Customer
from src.domain.regular_customer import RegularCustomer
from src.domain.premium_customer import PremiumCustomer
from src.domain.corporate_customer import CorporateCustomer


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
        customer_type = (data.get("customer_type") or "regular").strip().lower()

        cls_map = {
            "regular": RegularCustomer,
            "premium": PremiumCustomer,
            "corporate": CorporateCustomer,
        }
        cls = cls_map.get(customer_type, RegularCustomer)

        return cls(
            customer_id=data.get("customer_id"),
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone"),
            address=data.get("address"),
            active=data.get("active", True),
        )


