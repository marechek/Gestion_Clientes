from src.domain.customer import Customer

class PremiumCustomer(Customer):
    def __init__(self, **kwargs):
        kwargs["customer_type"] = "premium"
        super().__init__(**kwargs)

    def get_benefits(self) -> str:
        return "Cliente premium: beneficios premium."
