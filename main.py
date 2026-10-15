"""
Taller U3 - Automatización de BD con Python, Faker y Git
Autora: Walys Vera Herrera
"""
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text


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


def main():
    motor = crear_motor()
    probar_conexion(motor)


if __name__ == "__main__":
    main()