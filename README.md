# Sistema de Gestión de Clientes (Python + POO)

## Descripción
Sistema desarrollado en **Python 3** aplicando **Programación Orientada a Objetos (POO)** para la gestión de clientes.  
Permite crear, listar, editar y eliminar clientes, diferenciando tipos de clientes mediante **herencia, polimorfismo y abstracción**, validando datos de entrada, registrando actividad (logs) y persistiendo información en **archivos JSON**.

El proyecto está diseñado con una arquitectura **modular, escalable y mantenible**, separando claramente responsabilidades entre dominio, validaciones, servicios, persistencia y capa de interfaz.

---

## Objetivo general
Desarrollar una plataforma en Python basada en POO que permita gestionar clientes de forma estructurada, aplicando buenas prácticas de diseño de software y asegurando una base escalable y fácil de mantener.

---

## Objetivos específicos
- Diseñar un modelo UML detallado alineado con la implementación.
- Implementar un sistema de gestión de clientes aplicando:
  - Encapsulación
  - Herencia
  - Polimorfismo
  - Abstracción
- Incorporar validaciones avanzadas y manejo de errores estructurado.
- Implementar persistencia de datos mediante archivos JSON.
- Implementar pruebas unitarias para validar la funcionalidad del sistema.

---

## Funcionalidades
- Crear clientes.
- Listar clientes mediante **reporte tabular por consola**.
- Editar clientes existentes.
- Eliminar clientes.
- Diferenciación de tipos de cliente:
  - Regular
  - Premium
  - Corporate
- Validación de datos:
  - Email
  - Teléfono
  - Dirección
- Registro de actividad mediante logs.
- Persistencia de datos en archivo JSON.

---

## Conceptos POO aplicados

### Encapsulación
Los atributos sensibles (email, teléfono y dirección) se gestionan mediante propiedades (`@property` y setters), asegurando que los datos solo se modifiquen a través de validaciones controladas.

### Herencia
Las clases `RegularCustomer`, `PremiumCustomer` y `CorporateCustomer` heredan de la clase base `Customer`, reutilizando atributos y comportamiento común.

### Polimorfismo
Todas las subclases implementan el método `get_benefits()`, retornando beneficios distintos según el tipo de cliente, permitiendo tratar todos los clientes de forma uniforme desde el sistema.

### Abstracción
La clase `Customer` es una **clase abstracta**, que define el comportamiento común y el contrato que deben cumplir todos los tipos de clientes.  
El método `get_benefits()` se declara como abstracto, obligando a que cada subclase implemente su propia lógica, permitiendo trabajar con el concepto general de “cliente” sin depender de implementaciones concretas.

---

## Decisiones de Diseño y Arquitectura
El proyecto fue diseñado siguiendo principios de **arquitectura limpia** y **responsabilidad única (SRP)**.

Principales decisiones:
- Separación clara por capas (dominio, validaciones, servicios, persistencia, UI).
- Uso explícito de abstracción mediante clases base abstractas.
- Persistencia basada en archivos JSON para priorizar simplicidad y portabilidad.
- Implementación de un **reporte tabular por consola** en la capa de servicio (`CustomerService`), delegando la presentación a un único punto y evitando lógica condicional en la UI.
- Separación clara entre la interfaz de usuario y la lógica de negocio, manteniendo en el servicio únicamente lógica de normalización necesaria para la validación de entradas provenientes de la UI.

Estas decisiones permiten un sistema mantenible, extensible y fácil de comprender.

---

## Persistencia de datos
El sistema utiliza **archivos JSON** como mecanismo de persistencia principal.

- Archivo de datos: `data/customers.json`
- Características:
  - Autoincremento de identificadores
  - Serialización y deserialización de objetos
  - Reconstrucción automática del tipo de cliente

---

## Registro de actividad (Logging)
Las operaciones del sistema generan registros en archivos de log.

- Archivo: `logs/app.log`
- Se registran:
  - Creación, edición y eliminación de clientes
  - Listados de clientes
  - Errores de validación
  - Errores de persistencia
  
---

## Estructura del proyecto
```plaintext
gestion_clientes/
│
├── main.py
│
├── docs/
│ ├── poo_importancia.md
│ └── uml/
│  └── customer_mgn.puml
│
├── src/
│ ├── domain/
│ │ ├── customer.py
│ │ ├── regular_customer.py
│ │ ├── premium_customer.py
│ │ └── corporate_customer.py
│ │
│ ├── validators/
│ │ └── customer_validator.py
│ │
│ ├── persistence/
│ │ ├── customer_json_storage.py
│ │
│ ├── services/
│ │ ├── customer_service.py
│ │ └── customer_mapper.py
│ │
│ ├── ui/
│ │ └── menu.py
│ │
│ └── utils/
│ ├── exceptions.py
│ └── logger.py
│
├── tests/
│ ├── test_domain_customer.py
│ ├── test_service_json_crud.py
│ ├── test_validators.py
│ └── test_smoke.py
│
├── data/ # Persistencia local (ignorado por git)
├── logs/ # Logs del sistema (ignorado por git)
│
├── requirements.txt
├── .gitignore
└── README.md

```

---

### Descripción general
- **docs/**: documentación del proyecto (POO + UML).
- **src/**: código fuente organizado por responsabilidades.
- **tests/**: pruebas unitarias del sistema.
- **data/**: persistencia local (no versionada).
- **logs/**: registro de actividad del sistema (no versionado).

### Responsabilidades por capa
- **domain/**: entidades del negocio (clase Cliente + subclases).
- **validators/**: validaciones (email, teléfono, dirección).
- **persistence/**: persistencia JSON.
- **services/**: lógica de negocio (orquesta validación + repositorio).
- **ui/**: menú/consola (interacción con usuario).
- **utils/**: excepciones custom + logging.

---

## UML (alineado al código)

El diagrama UML del proyecto representa **fielmente la implementación actual del sistema** y se utiliza como documentación viva de la arquitectura.

- Archivo UML: `docs/uml/customer_mgn.puml`

**Criterios del diagrama**
- El UML refleja las clases, métodos y relaciones realmente implementadas.
- `Customer` se modela como clase abstracta que define el contrato común.
- Las dependencias y asociaciones se ajustan al flujo real del sistema.
- El *composition root* se encuentra en `main.py`, donde se instancian y conectan las dependencias principales (`AppLogger`, `CustomerJsonStorage`, `CustomerService` y `Menu`).

El objetivo del UML no es proponer un diseño teórico, sino documentar el estado real y funcional del sistema.

---

## Documentación POO
- Documento: `docs/poo_importancia.md`

---

## Requisitos
- Python 3.x
- Dependencias en `requirements.txt`

---

## Instalación
```bash
python -m pip install -r requirements.txt
```

---

## Ejecución
- python main.py

### Uso General del Sistema
Desde el menú por consola es posible realizar las siguientes acciones:

- **Crear cliente**  
  Permite registrar un nuevo cliente indicando su tipo (Regular, Premium o Corporate) y sus datos básicos.  
  El sistema valida automáticamente la información ingresada antes de persistirla.

- **Listar clientes**  
  Muestra todos los clientes registrados junto con su tipo y beneficios asociados.

- **Editar cliente**  
  Permite modificar los datos de un cliente existente.  
  Antes de realizar la edición, el sistema valida que el cliente exista.

- **Eliminar cliente**  
  Permite eliminar un cliente del sistema previa validación de existencia y confirmación del usuario.

- **Salir**  
  Finaliza la ejecución del sistema.

Todas las operaciones realizadas quedan registradas en los archivos de log del sistema.

---

## Pruebas Unitarias
- python -m pytest

---

## Manejo de errores
El sistema implementa un manejo de errores estructurado mediante excepciones personalizadas, asegurando que la aplicación no se detenga ante entradas inválidas o problemas de ejecución.

- Validaciones de datos:
  - Email con formato inválido
  - Teléfono incorrecto
  - Campos obligatorios vacíos
- Validación de operaciones:
  - Intento de edición o eliminación de clientes inexistentes
- Manejo de errores de persistencia:
  - Problemas de lectura o escritura del archivo JSON

Las excepciones personalizadas se definen en `src/utils/exceptions.py`, mientras que las validaciones de datos se centralizan en `src/validators`.

---

## Conclusiones Finales
Este proyecto demuestra la aplicación práctica de los principales conceptos de la Programación Orientada a Objetos en Python, integrando encapsulación, herencia, polimorfismo y abstracción en un sistema funcional.

La correcta separación de responsabilidades, junto con el uso de validaciones, servicios y persistencia desacoplada, permite que el sistema sea claro, mantenible y fácil de extender.

El diseño adoptado cumple con los objetivos del proyecto y se alinea con buenas prácticas de desarrollo de software.

---

## Autor

Proyecto académico desarrollado como parte del **Módulo 4 – Programación Avanzada en Python**, en el marco de la **Actividad Basada en Proyectos (ABP 4)**.

El proyecto fue diseñado, desarrollado, probado y documentado íntegramente por **Marcos Elias**, aplicando los contenidos y buenas prácticas abordadas durante el módulo.

---

## Posibles Mejoras Futuras
- Incorporar una base de datos relacional para mayor escalabilidad.
- Exponer la lógica del sistema mediante una API REST.
- Implementar autenticación y gestión de usuarios.
- Agregar una interfaz gráfica o aplicación web.
- Incorporar roles y permisos por tipo de usuario.
- Ampliar la cobertura de pruebas unitarias y agregar pruebas de integración.

