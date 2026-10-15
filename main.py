"""
Taller U3 - Automatización de BD con Python, Faker y Git
Autora: Walys Vera Herrera
"""
import os

from dotenv import load_dotenv
from sqlalchemy import (
    Column, Date, DateTime, Integer, MetaData, String, Table,
    create_engine, text,
)

NOMBRE_TABLA = "personas_walys"

# Estructura de la tabla: 1 clave primaria + 9 atributos que llenará Faker
metadata = MetaData()

personas = Table(
    NOMBRE_TABLA,
    metadata,
    Column("id_persona", Integer, primary_key=True, autoincrement=True),
    Column("nombre", String(60), nullable=False),
    Column("apellido", String(60), nullable=False),
    Column("correo", String(120), nullable=False),
    Column("telefono", String(30)),
    Column("fecha_nacimiento", Date),
    Column("ciudad", String(80)),
    Column("direccion", String(200)),
    Column("profesion", String(200)),
    Column("fecha_registro", DateTime),
)


def crear_motor():
    """Lee las credenciales del archivo .env y crea la conexión a MySQL."""
    load_dotenv()

    usuario = os.getenv("DB_USER")
    contrasena = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    puerto = os.getenv("DB_PORT")
    base_datos = os.getenv("DB_NAME")

    url = f"mysql+pymysql://{usuario}:{contrasena}@{host}:{puerto}/{base_datos}"
    return create_engine(url)


def probar_conexion(motor):
    """Hace una consulta sencilla para confirmar que la conexión funciona."""
    with motor.connect() as conn:
        version = conn.execute(text("SELECT VERSION()")).scalar()
        print(f"Conexión exitosa a MySQL (versión {version})")


def crear_tabla(motor):
    """Crea la tabla solo si todavía no existe en la base de datos."""
    metadata.create_all(motor)
    print(f"Tabla '{NOMBRE_TABLA}' lista.")


def main():
    motor = crear_motor()
    probar_conexion(motor)
    crear_tabla(motor)


if __name__ == "__main__":
    main()