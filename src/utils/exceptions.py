class AppError(Exception):
    """Error base de la aplicación."""
    pass


class ValidationError(AppError):
    """Error cuando una validación falla."""
    pass


class RequiredFieldError(ValidationError):
    """Error cuando faltan campos obligatorios."""
    pass


class DataAccessError(AppError):
    """Error de acceso a datos (DB/archivos)."""
    pass

