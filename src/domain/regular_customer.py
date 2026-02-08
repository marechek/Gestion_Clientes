from src.domain.customer import Customer


class RegularCustomer(Customer):
    def get_benefits(self) -> str:
        return "Cliente regular: acceso a promociones básicas."
