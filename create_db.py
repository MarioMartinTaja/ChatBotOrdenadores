import pyodbc
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Conexión a Azure SQL Database
conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={os.getenv("DB_SERVER")},{os.getenv("DB_PORT")};DATABASE={os.getenv("DB_NAME")};UID={os.getenv("DB_USER")};PWD={os.getenv("DB_PASSWORD")}'
)

cursor = conn.cursor()

# Crear la tabla con los nombres de los campos correctos
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ordenadores (
        id INT IDENTITY(1,1) PRIMARY KEY,
        Marca TEXT,
        Modelo TEXT,
        Precio NUMERIC,
        Codigo_Producto TEXT UNIQUE,
        Disco_Duro TEXT,
        Grafica TEXT,
        Procesador TEXT,
        Pantalla TEXT,
        Peso TEXT,
        RAM TEXT,
        Bateria TEXT,
        Sistema_Operativo TEXT
    );
""")

conn.commit()
cursor.close()
conn.close()
print("✅ Base de datos y tabla creadas correctamente con los nombres correctos.")
