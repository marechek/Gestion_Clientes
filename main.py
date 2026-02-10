from src.persistence.customer_json_storage import CustomerJsonStorage
from src.services.customer_service import CustomerService
from src.ui.menu import Menu
from src.services.logger_service import LoggerService


def main():
    logger = LoggerService.setup("logs/service.log")

    storage = CustomerJsonStorage("data/customers.json")
    service = CustomerService(storage)

    menu = Menu(service=service, logger=logger)
    menu.run()


if __name__ == "__main__":
    main()
