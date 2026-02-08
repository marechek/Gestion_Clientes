from src.persistence.json_storage import CustomerJsonStorage


class CustomerService:
    def __init__(self, storage: CustomerJsonStorage):
        self.storage = storage
