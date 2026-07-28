# 🏦 Sistema Bancario en Python

Proyecto desarrollado para consolidar conocimientos de Programación Orientada a Objetos (POO), aplicando principios de diseño, validaciones y organización modular del código.

El objetivo fue simular el funcionamiento básico de un banco aplicando buenas prácticas de diseño, separación de responsabilidades y validaciones de negocio.

---

## 🚀 Funcionalidades

- Crear clientes.
- Crear cuentas de ahorro.
- Crear cuentas corrientes.
- Depositar dinero.
- Retirar dinero.
- Transferir dinero entre cuentas.
- Consultar saldo.
- Listar clientes registrados.

---

## 📂 Estructura del proyecto

```
Poo-python/
│
├── main.py
├── modelos/
│   ├── banco.py
│   ├── cliente.py
│   ├── cuenta_bancaria.py
│   ├── cuenta_ahorros.py
│   └── cuenta_corriente.py
│
├── menu/
│   ├── menu.py
│   └── operaciones.py
│
└── utils/
    ├── entradas.py
    └── helpers.py
```

---

## 🧠 Conceptos aplicados

Durante el desarrollo del proyecto se aplicaron conceptos fundamentales de Programación Orientada a Objetos:

- Clases y Objetos
- Encapsulamiento
- Herencia
- Polimorfismo
- Composición
- Abstracción
- Validación de datos
- Manejo de excepciones (`try`, `except`, `raise`)
- Refactorización
- Organización modular del código
- Separación entre lógica de negocio e interfaz

---

## 🏛️ Arquitectura

El proyecto está organizado en capas simples:

- **modelos/** → Contiene toda la lógica del negocio.
- **menu/** → Gestiona la interacción con el usuario.
- **utils/** → Funciones auxiliares y validaciones de entrada.
- **main.py** → Punto de entrada de la aplicación.

Esta organización facilita el mantenimiento y futuras ampliaciones.

---

## 🛡️ Validaciones implementadas

- No permite clientes con el mismo correo.
- No permite clientes con el mismo teléfono.
- No permite crear cuentas para clientes inexistentes.
- No permite números de cuenta duplicados.
- No permite retirar fondos insuficientes.
- No permite transferencias a la misma cuenta.
- Validación de tipos de datos.
- Validación de montos positivos.
- Manejo de errores mediante excepciones.

---

## ▶️ Ejecución

Clonar el repositorio:

```bash
git clone "https://github.com/EFAM2907/Poo-python.git"
```

Entrar al proyecto:

```bash
cd Poo-python
```

Ejecutar:

```bash
python main.py
```

---

## 🛠️ Tecnologías

- Python 3
- Programación Orientada a Objetos
- Git
- GitHub

---

## 📚 Próximas mejoras

Este proyecto servirá como base para futuras versiones donde se implementará:

- Persistencia con SQLite.
- Arquitectura Hexagonal.
- Testing con pytest.
- API REST con FastAPI.

---

## 📷 Vista del programa

![Menú principal](docs/menu.png)

## 👨‍💻 Autor:
Edwin Fernando Arias Montoya
