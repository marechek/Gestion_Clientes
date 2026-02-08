from src.domain.customer import Customer

class CorporateCustomer(Customer):
    def __init__(self, **kwargs):
        kwargs["customer_type"] = "corporate"
        super().__init__(**kwargs)

    def get_benefits(self) -> str:
        return "Cliente corporativo: beneficios corporativo."
