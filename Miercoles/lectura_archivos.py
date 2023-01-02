# Función open(file, mode)
# mode:
# r -> Leer - Lectura
# x -> Crea el archivo, si existe ya el archivo retorna un error
archivo = open('prueba.txt', 'r')
# Al abrir un archivo en modo lectura, tenemos 2 funciones:
# read() -> Retornara el contenido del archivo
# print(archivo.read())
# seek() -> Debes indicar a la posición donde quieres ir (cursor)
# archivo.seek(0)
# readlines() -> Retorna una lista con los valores por linea
# print(archivo.readlines())
for linea in archivo:
    print(linea)

# Cerramos el archivo gestionado
archivo.close()
