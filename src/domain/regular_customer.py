from src.domain.customer import Customer

class RegularCustomer(Customer):
    def __init__(self, **kwargs):
        kwargs["customer_type"] = "regular"
        super().__init__(**kwargs)

    def get_benefits(self) -> str:
        return "Cliente regular: sin beneficios adicionales."
