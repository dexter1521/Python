import random
import csv
from faker import Faker

# Crear instancia de Faker para generar datos aleatorios
fake = Faker()

# Lista de cursos
cursos = ['Python', 'JavaScript', 'Java', 'C++', 'HTML/CSS', 'SQL']

# Función para generar datos de ejemplo
def generar_datos(num_registros):
    datos = []
    for _ in range(num_registros):
        nombre = fake.name()
        mail = fake.email()
        curso = random.choice(cursos)
        all_star = random.choice(['Si', 'No'])
        datos.append([nombre, mail, curso, all_star])
    return datos

# Función para escribir datos en un archivo CSV
def escribir_csv(nombre_archivo, datos):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['Nombre', 'Mail', 'Curso', 'All-Star'])
        escritor.writerows(datos)

# Generar 100 registros de ejemplo
registros = generar_datos(100)

# Escribir los datos en un archivo CSV llamado "alumnos.csv"
escribir_csv('alumnos.csv', registros)
