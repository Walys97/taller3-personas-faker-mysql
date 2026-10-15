# Taller U3 - Base de datos con Python, Faker y Git

- **Estudiante:** Walys Vera Herrera
- **Curso:** Bases de Datos para Ciencia de Datos - UdeA
- **Profesor:** Miguel Ramos García

## Qué hace el proyecto

En este taller hice un script en Python (`main.py`) que:

- Se conecta a mi base de datos MySQL local usando SQLAlchemy.
- Crea la tabla `personas_walys` si todavía no existe.
- Llena la tabla con 100.000 personas inventadas usando la librería Faker.
- Al final cuenta los registros para comprobar que sí quedaron los 100.000.

Los datos de conexión (usuario y contraseña) no están en el código, los leo desde un archivo `.env` con python-dotenv. Ese archivo no se sube al repositorio, por eso dejé un `.env.example` como plantilla.

Para que no fuera tan lento, inserto los registros en grupos de 10.000 en vez de uno por uno.

## Columnas de la tabla

`id_persona` (llave primaria), `nombre`, `apellido`, `correo`, `telefono`, `fecha_nacimiento`, `ciudad`, `direccion`, `profesion` y `fecha_registro`.

## Cómo instalarlo

1. Crear el entorno virtual y activarlo:
```
python -m venv .venv
.venv\Scripts\activate
```

2. Instalar las librerías:
```
pip install -r requirements.txt
```

3. Crear la base de datos en MySQL (yo lo hice en DBeaver):
```sql
CREATE DATABASE taller3_walys;
```

4. Copiar el archivo `.env.example`, renombrarlo como `.env` y poner el usuario y la contraseña de MySQL.

## Cómo ejecutarlo

```
python main.py
```

Esto fue lo que me salió cuando lo ejecuté:

```
Conexión exitosa a MySQL (versión 8.0.46)
Tabla 'personas_walys' lista.
  Insertados 10,000 de 100,000
  Insertados 20,000 de 100,000
  ...
  Insertados 100,000 de 100,000
Inserción terminada en 70.8 segundos.
Total de registros en 'personas_walys': 100,000
```

Para verificarlo en DBeaver usé:

```sql
SELECT COUNT(*) FROM personas_walys;
```