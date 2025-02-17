import os
import requests
import json
from dotenv import load_dotenv

# Cargar credenciales desde el .env
load_dotenv()
endpoint = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT")
api_key = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_KEY")
model_id = os.getenv("AZURE_CUSTOM_MODEL_ID")

# Ruta donde están los PDFs
pdf_folder = "pdfs/"
output_folder = "output_texts/"
os.makedirs(output_folder, exist_ok=True)

def extract_text_from_pdf(pdf_path):
    """Extrae datos de un PDF usando un modelo personalizado de Azure Document Intelligence"""
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()

    url = f"{endpoint}/documentModels/{model_id}:analyze?api-version=2023-07-31"
    headers = {
        "Ocp-Apim-Subscription-Key": api_key,
        "Content-Type": "application/pdf"
    }

    response = requests.post(url, headers=headers, data=pdf_data)
    result = response.json()

    # Guardar el JSON extraído en un archivo
    output_file = os.path.join(output_folder, os.path.basename(pdf_path).replace(".pdf", ".json"))
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"✅ Datos extraídos y guardados en {output_file}")
    return result

# Extraer todos los PDFs en la carpeta
for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith(".pdf"):
        extract_text_from_pdf(os.path.join(pdf_folder, pdf_file))
