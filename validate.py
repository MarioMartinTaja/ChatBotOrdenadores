import json
import os

def validate_data(json_file):
    """Valida los datos extraídos desde un archivo JSON asegurando que contenga los campos necesarios."""
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    required_fields = ["Marca", "Modelo", "Precio", "Codigo Producto", "Disco Duro", "Grafica", "Procesador", "Pantalla", "Peso", "RAM", "Bateria", "Sistema Operativo"]
    
    missing_fields = [field for field in required_fields if field not in data or not data[field]]
    
    if missing_fields:
        print(f"⚠️ Datos incompletos en {json_file}: Faltan {missing_fields}")
        return False

    print(f"✅ {json_file} validado correctamente")
    return True

# Validar todos los archivos en output_texts/
output_folder = "output_texts/"
for json_file in os.listdir(output_folder):
    if json_file.endswith(".json"):
        validate_data(os.path.join(output_folder, json_file))
