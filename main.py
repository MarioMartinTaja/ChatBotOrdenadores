import os
import extract
import create_db
import validate
import insert_data

# 1️⃣ Extraer datos de los PDFs
pdf_folder = "pdfs/"
for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith(".pdf"):
        extract.extract_text_from_pdf(os.path.join(pdf_folder, pdf_file))

# 2️⃣ Crear la base de datos si no existe
create_db

# 3️⃣ Validar los datos extraídos
output_folder = "output_texts/"
valid_files = []
for json_file in os.listdir(output_folder):
    if json_file.endswith(".json") and validate.validate_data(os.path.join(output_folder, json_file)):
        valid_files.append(json_file)

print(f"📂 {len(valid_files)} archivos validados correctamente. Listos para insertar en la base de datos.")

# 4️⃣ Insertar los datos en la base de datos
if valid_files:
    insert_data
