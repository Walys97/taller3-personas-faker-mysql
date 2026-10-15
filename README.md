# Taller U3 — Automatización de BD con Python, Faker y Git

**Autora:** Walys Vera Herrera
**Curso:** Bases de Datos para Ciencia de Datos — Universidad de Antioquia
**Docente:** Miguel Ramos García

## ¿Qué hace este proyecto?

El script `main.py` automatiza la creación y el poblado de una base de datos MySQL local:

1. Lee las credenciales de conexión desde un archivo `.env` (con `python-dotenv`), para no escribir la contraseña en el código.
2. Se conecta a MySQL con `create_engine` de **SQLAlchemy** (driver `pymysql`).
3. Crea automáticamente la tabla `personas_walys` si no existe.
4. Genera **100.000 personas ficticias** con **Faker** (en español de Colombia, `es_CO`) como una lista de diccionarios.
5. Inserta los registros **por lotes de 10.000** usando `conn.execute()`, lo que es mucho más rápido que insertar uno por uno.
6. Al final cuenta los registros para verificar que quedaron 100.000.

## Estructura de la tabla `personas_walys`

| Columna | Tipo | Generado con Faker |
|---|---|---|
| `id_persona` | INT, **PK**, autoincremental | — |
| `nombre` | VARCHAR(60) | `first_name()` |
| `apellido` | VARCHAR(60) | `last_name()` |
| `correo` | VARCHAR(120) | `email()` |
| `telefono` | VARCHAR(30) | `phone_number()` |
| `fecha_nacimiento` | DATE | `date_of_birth(18, 80)` |
| `ciudad` | VARCHAR(80) | `city()` |
| `direccion` | VARCHAR(200) | `address()` |
| `profesion` | VARCHAR(200) | `job()` |
| `fecha_registro` | DATETIME | `date_time_between("-3y", "now")` |

## Estructura del proyecto

```
├── main.py            # Script principal
├── requirements.txt   # Librerías necesarias
├── .env.example       # Plantilla de variables de entorno
├── .gitignore         # Archivos que Git no debe subir
└── README.md
```

## Requisitos previos

- Python 3.10 o superior
- MySQL 8 corriendo en local
- Git

## Instalación

1. Clonar el repositorio y entrar a la carpeta:
```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DE_LA_CARPETA>
```

2. Crear y activar el entorno virtual:
```bash
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   source .venv/bin/activate     # Mac / Linux
```

3. Instalar las dependencias:
```bash
   pip install -r requirements.txt
```

4. Crear la base de datos en MySQL (por ejemplo, desde DBeaver):
```sql
   CREATE DATABASE IF NOT EXISTS taller3_walys;
```

5. Copiar `.env.example` como `.env` y completar los datos reales de conexión:
```
   DB_USER=tu_usuario
   DB_PASSWORD=tu_contrasena
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=taller3_walys
```
   > El archivo `.env` está en el `.gitignore`, así que las credenciales reales nunca se suben al repositorio.

## Ejecución

Con el entorno virtual activado, ejecutar:

```bash
python main.py
```

Salida esperada:

```
Conexión exitosa a MySQL (versión 8.0.46)
Tabla 'personas_walys' lista.
  Insertados 10,000 de 100,000
  ...
  Insertados 100,000 de 100,000
Inserción terminada en XX.X segundos.
Total de registros en 'personas_walys': 100,000
```

## Verificación

En DBeaver se puede comprobar el total con:

```sql
SELECT COUNT(*) FROM personas_walys;
```