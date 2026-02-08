import json
from pathlib import Path
from src.utils.exceptions import DataAccessError


class CustomerJsonStorage:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self) -> dict:
        """
        Estructura esperada:
        {
          "last_id": 0,
          "customers": [ ... ]
        }
        """
        if not self.file_path.exists():
            return {"last_id": 0, "customers": []}

        try:
            with self.file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)

            # Si el archivo viene mal formado
            if not isinstance(data, dict):
                return {"last_id": 0, "customers": []}
            if "last_id" not in data or "customers" not in data:
                return {"last_id": 0, "customers": []}
            if not isinstance(data["customers"], list):
                data["customers"] = []

            return data
        except Exception as e:
            raise DataAccessError(f"Error al leer archivo JSON: {e}")

    def save(self, data: dict) -> None:
        try:
            # Asegurar carpeta
            self.file_path.parent.mkdir(parents=True, exist_ok=True)

            with self.file_path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            raise DataAccessError(f"Error al escribir archivo JSON: {e}")

