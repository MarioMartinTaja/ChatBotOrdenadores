import os
import json
import pyodbc
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Configurar conexión a Azure SQL Database
conn_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={os.getenv("DB_SERVER")},{os.getenv("DB_PORT")};DATABASE={os.getenv("DB_NAME")};UID={os.getenv("DB_USER")};PWD={os.getenv("DB_PASSWORD")}'

def insert_data(json_file):
    """Inserta datos desde un archivo JSON validado en la base de datos."""
    try:
        conn = pyodbc.connect(conn_string)
        cursor = conn.cursor()

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        query = """
        INSERT INTO ordenadores (Marca, Modelo, Precio, Codigo_Producto, Disco_Duro, Grafica, Procesador, Pantalla, Peso, RAM, Bateria, Sistema_Operativo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        values = (
            data.get("Marca"),
            data.get("Modelo"),
            data.get("Precio"),
            data.get("Codigo Producto"),
            data.get("Disco Duro"),
            data.get("Grafica"),
            data.get("Procesador"),
            data.get("Pantalla"),
            data.get("Peso"),
            data.get("RAM"),
            data.get("Bateria"),
            data.get("Sistema Operativo"),
        )

        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
        print(f"✅ Datos insertados correctamente desde {json_file}")

    except Exception as e:
        print(f"❌ Error al insertar datos en la base de datos: {e}")

# Insertar todos los archivos JSON validados
output_folder = "output_texts/"
for json_file in os.listdir(output_folder):
    if json_file.endswith(".json"):
        insert_data(os.path.join(output_folder, json_file))
