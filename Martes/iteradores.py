# foreach - for

meses = ["Enero", "Febrero", "Marzo"]

# for mes in meses:
#     print(mes)
#     if mes == "Febrero":
#         break
# print(f'fuera del scope -> {mes}')

# Obtener el indice y el valor
# for index, value in enumerate(meses):
#     print(index, value)

# for(x=0; x>10; x++)
# range -> 3 argumentos
# 1º Valor donde empieza
# 2º Hasta donde finalizara
# 3º De cuanto en cuanto incrementara

# Ejemplo:
# Recorrer nuestra edad y mostrar desde el año de nacimiento que año teniamos, hasta el año actual.
# edad = 28
# anio_naciste = 1994
#
# for anio, value in enumerate(range(edad), start=1995):
#     print(f'En el año {anio} tenias {value + 1} años')

# Ejemplo 2
persona = {
    "nombre": "Luis",
    "apellidos": "Lopez"
}

# keys
# for key in persona.keys():
#    print(key, persona[key])

# values
# for value in persona.values():
#    print(value)

# items
# for key, value in persona.items():
#     print(key, value)

# while
edad = 33

while edad > 18:
    print(f'edad -> {edad}')
    edad -= 1

    if edad == 21:
        break
