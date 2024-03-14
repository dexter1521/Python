import pandas as pd

# Leer el archivo de datos
alumnos = pd.read_csv('D:/htdocs/Python/Pandas/data/alumnos.csv')
alumnos.columns #listar las columnas


def get_user_info(i):
    nombre = alumnos.iloc[i]['Nombre']
    mail = alumnos.iloc[i]['Mail']
    allstar = alumnos.iloc[i]['All-Star']
    print(f'Nombre: {nombre}\nMail: {mail}\nAll-Star: {allstar}\n')  
    if allstar == "No":
        print(f'Hola {nombre}, hemos notado que no has sido un All-Star, te invitamos a que te esfuerces más para la próxima vez.\n')
        print(f'Recuerda que el esfuerzo y la dedicación son la clave para el éxito.\n')
        print(f'Saludos, el equipo de All-Star\n')
        print(f'Enviando mail a {mail}...\n')
    
get_user_info(0)