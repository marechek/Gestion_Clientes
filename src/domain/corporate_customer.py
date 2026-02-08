from src.domain.customer import Customer


class CorporateCustomer(Customer):
    def get_benefits(self) -> str:
        return "Cliente corporativo: precios preferenciales y soporte dedicado."
