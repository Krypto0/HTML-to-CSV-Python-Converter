import pandas as pd
import sqlite3
import os

# Ruta al archivo CSV combinado
csv_file_path = 'D:\\Downloads\\html-csv\\all_prospects.csv'  # Cambia esta ruta a la ubicación de tu archivo CSV combinado
sql_file_path = 'D:\\Downloads\\html-csv\\all_prospects.sql'  # Cambia esta ruta a donde quieres guardar tu archivo SQL

# Leer el archivo CSV en un DataFrame de pandas
df = pd.read_csv(csv_file_path)

# Conectar a la base de datos SQLite (creará una nueva base de datos)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Crear una tabla y cargar los datos del DataFrame
table_name = 'prospects'
df.to_sql(table_name, conn, if_exists='replace', index=False)

# Función para crear una instrucción SQL de creación de tabla
def create_table_sql(table_name, df):
    sql = f"CREATE TABLE {table_name} ("
    for col in df.columns:
        col_name = col.replace(' ', '_')  # Reemplazar espacios por guiones bajos en los nombres de las columnas
        sql += f"{col_name} TEXT,"
    sql = sql.rstrip(',')  # Eliminar la última coma
    sql += ");"
    return sql

# Generar las instrucciones SQL para crear la tabla y los datos
create_table_statement = create_table_sql(table_name, df)
inserts = []
for line in conn.iterdump():
    if line.startswith('INSERT INTO'):
        inserts.append(line)

# Guardar las instrucciones SQL en un archivo
with open(sql_file_path, 'w') as sql_file:
    sql_file.write(f"-- SQL script to create {table_name} table and insert data\n")
    sql_file.write(create_table_statement + "\n")
    for insert in inserts:
        insert = insert.replace('INSERT INTO "{}"'.format(table_name), 'INSERT INTO {}'.format(table_name))
        sql_file.write(insert + "\n")

# Cerrar la conexión
conn.close()

print(f'Archivo SQL creado en: {sql_file_path}')