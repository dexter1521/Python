import pandas as pd

# Leer el archivo de datos
cursos = pd.read_csv('D:/htdocs/Python/Pandas/data/cursos.csv')

intesivos = cursos[cursos['Sesiones'] <= 6]

intesivos #listar todos los cursos intesivos

report = cursos.sort_values(by='Curso')
report

