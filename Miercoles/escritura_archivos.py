from json import dump, loads

# mode:
# a -> Modifica el contenido el archivo, manteniendo los cambios anteriores
# w -> Reemplaza todo el contenido del archivo

# r+ -> Lee y escribe el archivo (Reemplaza todo el contenido)

# Implementación con archivo (txt)
#archivo = open('prueba.txt', 'a')
# Una vez abierto el archivo tenemos dos funciones a utilizar:
# write -> Enviar un solo valor
#archivo.write('Eduardo Argote\n')
# writelines -> Enviar mas de un valor (lista)
#archivo.writelines(['Daniel Silva\n', 'Diego Hernandez\n'])
# archivo.close()

# with open('prueba.txt', 'a') as archivo:
#    archivo.write('Eduardo Argote\n')

# Implementación con archivo (json)
data = [
    {
        'nombre': 'Brayan',
        'apellido': 'Acuna'
    },
    {
        'nombre': 'Bruno',
        'apellido': 'Calderon'
    },
    {
        'nombre': 'Daniel',
        'apellido': 'Silva'
    }
]

# with open('alumnos.json', 'w') as archivo:
#     dump(data, archivo, indent=4)

# Leer y Escribir un json
with open('alumnos.json', 'r+') as archivo:
    lectura = archivo.read()
    # Es traido como un string
    print(type(lectura))
    # Cargar el string a un diccionario
    cargar_data = loads(lectura)
    print(type(cargar_data))
    print(cargar_data)

    cargar_data.append({
        "nombre": "Diego",
        "apellido": "Hernandez"
    })

    archivo.seek(0)
    dump(cargar_data, archivo, indent=4)
