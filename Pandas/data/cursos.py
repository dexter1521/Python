import random
import csv
from faker import Faker
import os

# Crear instancia de Faker para generar datos aleatorios
fake = Faker()

# Lista de cursos
cursos = ['Python', 'JavaScript', 'Java', 'C++', 'HTML/CSS', 'SQL']

# Función para generar datos de ejemplo
def generar_datos(num_registros):
    datos = []
    for _ in range(num_registros):
        id = fake.random_number(digits=5)
        curso = random.choice(cursos)
        profesor = fake.name()
        comienzo = fake.date_this_decade()
        sesiones = random.randint(5, 20)
        datos.append([id, curso, profesor, comienzo, sesiones])
    return datos

# Función para escribir datos en un archivo CSV
def escribir_csv(nombre_archivo, datos):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['ID', 'Curso', 'Profesor', 'Comienzo', 'Sesiones'])
        escritor.writerows(datos)

# Obtener el directorio actual de trabajo
directorio_actual = os.getcwd()

# Generar 100 registros de ejemplo
registros = generar_datos(100)

# Nombre del archivo CSV
nombre_archivo = 'cursos.csv'

# Ruta completa del archivo CSV
ruta_archivo = os.path.join(directorio_actual, nombre_archivo)

# Escribir los datos en un archivo CSV en el directorio actual
escribir_csv(ruta_archivo, registros)
