from src.persistence.customer_json_storage import CustomerJsonStorage
from src.services.customer_service import CustomerService


def test_create_list_update_delete(tmp_path):
    file_path = tmp_path / "customers.json"
    storage = CustomerJsonStorage(str(file_path))
    service = CustomerService(storage)

    # Crear
    c1 = service.create_customer(
        customer_type="premium",
        name="Juan",
        email="juan@test.com",
        phone="12345678",
        address="Direccion valida"
    )
    assert c1.customer_id == 1

    # Listar
    customers = service.list_customers()
    assert len(customers) == 1

    # Actualizar
    updated = service.update_customer(1, name="Juan Perez", customer_type="corporate")
    assert updated is not None
    assert updated.name == "Juan Perez"
    assert "corporativo" in updated.get_benefits().lower()

    # Eliminar
    ok = service.delete_customer(1)
    assert ok is True
    assert service.list_customers() == []
