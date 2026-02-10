import logging
from pathlib import Path


class LoggerService:
    @staticmethod
    def setup(log_file: str = "logs/app.log") -> logging.Logger:
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)

        logger = logging.getLogger("customer_app")
        logger.setLevel(logging.INFO)

        # Evita handlers duplicados si se llama más de una vez
        if not logger.handlers:
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger