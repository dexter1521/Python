import pandas as pd

# Leer el archivo de datos
#df = pd.read_excel('cursos.xlsx')

cursos = pd.read_csv('D:/htdocs/Python/Pandas/data/cursos.csv')
alumnos = pd.read_csv('D:/htdocs/Python/Pandas/data/alumnos.csv')


cursos #listar todos los archivos

cursos.head() #listar los primeros 5 archivos

cursos.tail() #listar los ultimos 5 archivos

alumnos.columns #listar las columnas

print(alumnos['Nombre']) #listar la columna nombre

# Obtener la longitud de la columna 'Nombre'
longitud_nombre = len(alumnos['Nombre'])
print(longitud_nombre)