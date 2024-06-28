from bs4 import BeautifulSoup
import pandas as pd
import os

# Ruta a la carpeta con los archivos HTML
html_folder_path = 'D:\\Downloads\\html-csv\\html_files'  # Cambia esta ruta a la ubicación de tu carpeta de archivos HTML
csv_file_path = 'D:\\Downloads\\html-csv\\all_prospects.csv'  # Cambia esta ruta a donde quieres guardar el archivo CSV combinado

# Lista para almacenar todos los prospectos
all_prospects = []

# Función para convertir un archivo HTML a un diccionario de prospecto
def extract_prospects_from_html(html_file_path):
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    prospect_sections = soup.find_all("div", class_="prospect-details")

    for section in prospect_sections:
        name = section.find("div", class_="prospect-name").text.strip()
        email = section.find("div", class_="prospect-email").find("span", class_="email-txt").text.strip()
        status = section.find("div", class_="prospect-status").find("span", class_="label").text.strip()
        created_date = section.find("div", class_="prospect-date").find_all("span")[-1].text.strip()
        source = section.find("div", class_="prospect-source").text.split(":")[-1].strip()
        owned_by = section.find("div", class_="prospect-owned-by").find_all("span")[-1].text.strip()
        category = section.find("div", class_="prospect-category").find_all("span")[-1].text.strip()
        tag = section.find("div", class_="prospect-tags").find_all("span")[-1].text.strip()

        all_prospects.append({
            "Name": name,
            "Email": email,
            "Status": status,
            "Created Date": created_date,
            "Source": source,
            "Owned By": owned_by,
            "Category": category,
            "Tag": tag
        })

# Procesar todos los archivos HTML en la carpeta
for filename in os.listdir(html_folder_path):
    if filename.endswith('.html'):
        html_file_path = os.path.join(html_folder_path, filename)
        extract_prospects_from_html(html_file_path)
        print(f'Procesado: {html_file_path}')

# Crear un DataFrame de pandas con todos los prospectos
prospects_df = pd.DataFrame(all_prospects)

# Guardar el DataFrame en un único archivo CSV
prospects_df.to_csv(csv_file_path, index=False)

print(f'Archivo CSV combinado creado en: {csv_file_path}')