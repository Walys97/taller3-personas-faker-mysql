"""
Taller U3 - Automatización de BD con Python, Faker y Git
Autora: Walys Vera Herrera
"""
import os
import time

from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import (
    Column, Date, DateTime, Integer, MetaData, String, Table,
    create_engine, func, insert, select, text,
)

NOMBRE_TABLA = "personas_walys"
TOTAL_REGISTROS = 100_000
TAMANO_LOTE = 10_000  # se insertan de a 10.000 filas por vez

# Faker configurado en español de Colombia
fake = Faker("es_CO")

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


def generar_persona():
    """Genera un diccionario con los datos falsos de una persona."""
    return {
        "nombre": fake.first_name(),
        "apellido": fake.last_name(),
        "correo": fake.email(),
        "telefono": fake.phone_number(),
        "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=80),
        "ciudad": fake.city(),
        "direccion": fake.address().replace("\n", ", "),
        "profesion": fake.job(),
        "fecha_registro": fake.date_time_between(start_date="-3y", end_date="now"),
    }


def insertar_registros(motor):
    """Borra lo que hubiera y luego inserta los 100.000 registros por lotes."""
    inicio = time.time()
    with motor.begin() as conn:
        # Vacía la tabla para que, si se corre de nuevo, queden 100.000 exactos
        conn.execute(personas.delete())

        for i in range(0, TOTAL_REGISTROS, TAMANO_LOTE):
            lote = [generar_persona() for _ in range(TAMANO_LOTE)]
            conn.execute(insert(personas), lote)  # inserción por lotes
            print(f"  Insertados {i + TAMANO_LOTE:,} de {TOTAL_REGISTROS:,}")

    print(f"Inserción terminada en {time.time() - inicio:.1f} segundos.")


def contar_registros(motor):
    """Cuenta cuántas filas quedaron en la tabla."""
    with motor.connect() as conn:
        total = conn.execute(select(func.count()).select_from(personas)).scalar()
    print(f"Total de registros en '{NOMBRE_TABLA}': {total:,}")


def main():
    motor = crear_motor()
    probar_conexion(motor)
    crear_tabla(motor)
    insertar_registros(motor)
    contar_registros(motor)


if __name__ == "__main__":
    main()