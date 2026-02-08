from src.utils.exceptions import ValidationError, RequiredFieldError, DataAccessError


class Menu:
    def __init__(self, **kwargs):
        self.service = kwargs.get("service")
        self.logger = kwargs.get("logger")

    def run(self):
        while True:
            self._print_menu()
            option = input("Selecciona una opción: ").strip()

            if option == "1":
                self._create_customer()
            elif option == "2":
                self._list_customers()
            elif option == "3":
                self._update_customer()
            elif option == "4":
                self._delete_customer()
            elif option == "0":
                print("Saliendo...")
                self.logger.info("APP_EXIT | Usuario salió del sistema.")
                break
            else:
                print("Opción inválida.")
                self.logger.warning("INVALID_OPTION | Opción inválida ingresada.")

    def _print_menu(self):
        print("\n=== Gestión de Clientes ===")
        print("1) Crear cliente")
        print("2) Listar clientes")
        print("3) Editar cliente")
        print("4) Eliminar cliente")
        print("0) Salir")

    def _create_customer(self):
        try:
            print("Tipo de cliente:")
            print("1) Regular")
            print("2) Premium")
            print("3) Corporate")

            raw_type = input("Selecciona tipo (1/2/3 o regular/premium/corporate): ")
            name = input("Nombre: ").strip()
            email = input("Email: ").strip()
            phone = input("Teléfono: ").strip()
            address = input("Dirección: ").strip()

            customer = self.service.create_customer_from_input(
                raw_customer_type=raw_type,
                name=name,
                email=email,
                phone=phone,
                address=address
            )

            print(f"Cliente creado: {customer}")
            print(customer.get_benefits())
            self.logger.info(f"CREATE | customer_id={customer.customer_id}")

        except (ValidationError, RequiredFieldError) as e:
            print(f"Error de validación: {e}")
            self.logger.warning(f"VALIDATION_ERROR_CREATE | {e}")

        except DataAccessError as e:
            print(f"Error de persistencia: {e}")
            self.logger.error(f"DATA_ACCESS_ERROR_CREATE | {e}")

    def _list_customers(self):
        try:
            customers = self.service.list_customers()
            if not customers:
                print("No hay clientes registrados.")
                self.logger.info("LIST | sin registros")
                return

            print("\n--- Clientes ---")
            for c in customers:
                print(f"- {c} | Beneficios: {c.get_benefits()}")
            self.logger.info(f"LIST | total={len(customers)}")

        except DataAccessError as e:
            print(f"Error de persistencia: {e}")
            self.logger.error(f"DATA_ACCESS_ERROR_LIST | {e}")

    def _update_customer(self):
        try:
            raw_id = input("ID del cliente a editar: ").strip()

            print("Deja en blanco para no modificar.")
            name = input("Nuevo nombre: ").strip() or None
            email = input("Nuevo email: ").strip() or None
            phone = input("Nuevo teléfono: ").strip() or None
            address = input("Nueva dirección: ").strip() or None

            print("Tipo de cliente (opcional):")
            print("1) Regular")
            print("2) Premium")
            print("3) Corporate")
            raw_type = input("Nuevo tipo (1/2/3 o regular/premium/corporate) [Enter para no cambiar]: ").strip() or None

            updated = self.service.update_customer_from_input(
                raw_customer_id=raw_id,
                raw_customer_type=raw_type,
                name=name,
                email=email,
                phone=phone,
                address=address
            )

            if updated is None:
                print("Cliente no encontrado.")
                self.logger.info(f"UPDATE_NOT_FOUND | input_id={raw_id}")
                return

            print(f"Cliente actualizado: {updated}")
            print(updated.get_benefits())
            self.logger.info(f"UPDATE | customer_id={updated.customer_id}")

        except (ValidationError, RequiredFieldError) as e:
            print(f"Error de validación: {e}")
            self.logger.warning(f"VALIDATION_ERROR_UPDATE | {e}")

        except DataAccessError as e:
            print(f"Error de persistencia: {e}")
            self.logger.error(f"DATA_ACCESS_ERROR_UPDATE | {e}")

    def _delete_customer(self):
        try:
            raw_id = input("ID del cliente a eliminar: ").strip()

            ok = self.service.delete_customer_from_input(raw_customer_id=raw_id)
            if ok:
                print("Cliente eliminado.")
                self.logger.info(f"DELETE | input_id={raw_id}")
            else:
                print("Cliente no encontrado.")
                self.logger.info(f"DELETE_NOT_FOUND | input_id={raw_id}")

        except ValidationError as e:
            print(f"Error de validación: {e}")
            self.logger.warning(f"VALIDATION_ERROR_DELETE | {e}")

        except DataAccessError as e:
            print(f"Error de persistencia: {e}")
            self.logger.error(f"DATA_ACCESS_ERROR_DELETE | {e}")

