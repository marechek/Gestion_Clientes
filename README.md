# Sistema de Gestión de Clientes (Python + POO)

## Descripción
Plataforma desarrollada en **Python 3** aplicando **Programación Orientada a Objetos (POO)** para gestionar clientes, validar datos, registrar actividad (logs) y persistir información usando **SQLite** y archivos **JSON/CSV**.  
El sistema está diseñado con una estructura **modular, escalable y segura**.

## Objetivo general
Desarrollar una plataforma en Python basada en POO, que permita gestionar clientes, realizar validaciones en línea e integrarse con servicios externos, asegurando una estructura modular, escalable y segura.

## Objetivos específicos
- Diseñar un modelo UML detallado del sistema.
- Implementar un sistema de gestión de clientes con herencia, polimorfismo y encapsulación.
- Incorporar validaciones avanzadas y manejo de errores estructurado.
- Implementar persistencia de datos con SQLite y archivos JSON/CSV.
- Implementar pruebas unitarias para validar la funcionalidad.

## Funcionalidades esenciales
- Gestión de clientes: creación, edición y eliminación.
- Diferenciación de tipos: ClienteRegular, ClientePremium, ClienteCorporativo.
- Validaciones de atributos: email, teléfono y dirección.
- Persistencia de datos: SQLite + JSON (y CSV si aplica).
- Registro de actividad: logs de operaciones realizadas.

## Estructura del proyecto
gestion_clientes/
│
├── main.py
│
├── docs/
│ ├── poo_importancia.md
│ └── uml/
│ └── modelo.puml
│
├── src/
│ ├── domain/
│ ├── validators/
│ ├── persistence/
│ ├── services/
│ ├── ui/
│ └── utils/
│
├── tests/
│
├── data/ # Local, ignorado por git (SQLite / JSON / CSV)
├── logs/ # Local, ignorado por git (archivos de log)
│
├── requirements.txt
├── .gitignore
└── README.md

### Descripción general
- **docs/**: documentación del proyecto (POO + UML).
- **src/**: código fuente organizado por responsabilidades.
- **tests/**: pruebas unitarias del sistema.
- **data/**: persistencia local (no versionada).
- **logs/**: registro de actividad del sistema (no versionado).

### Responsabilidades por capa
- **domain/**: entidades del negocio (clase Cliente + subclases).
- **validators/**: validaciones (email, teléfono, dirección).
- **persistence/**: persistencia SQLite + JSON/CSV.
- **services/**: lógica de negocio (orquesta validación + repositorio).
- **ui/**: menú/consola (interacción con usuario).
- **utils/**: excepciones custom + logging.

## UML
- Archivo UML: `docs/uml/modelo.puml`

## Documentación POO
- Documento: `docs/poo_importancia.md`

## Requisitos
- Python 3.x
- Dependencias en `requirements.txt`

## Instalación
```bash
python -m pip install -r requirements.txt
```

## Ejecución
- python main.py

## Pruebas Unitarias
- python -m pytest

## Manejo de errores y logging
- Logs (local): logs/app.log
- Validaciones y excepciones personalizadas se implementan en src/validators y src/utils.