from src.domain.customer import Customer


class PremiumCustomer(Customer):
    def get_benefits(self) -> str:
        return "Cliente premium: descuentos exclusivos y atención prioritaria."
