import json
from pathlib import Path
from src.utils.exceptions import DataAccessError


class CustomerJsonStorage:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self) -> list[dict]:
        if not self.file_path.exists():
            return []

        try:
            with self.file_path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            raise DataAccessError(f"Error al leer archivo JSON: {e}")

    def save(self, data: list[dict]) -> None:
        try:
            with self.file_path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            raise DataAccessError(f"Error al escribir archivo JSON: {e}")
