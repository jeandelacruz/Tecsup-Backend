# Estructuras de datos
# Mutables - Inmutables

# Array - > JS
# Lista (list) -> Mutable
# Formula: n - 1
# Valores       0        1         2
personas = ["Brayan", "Bruno", "Daniel"]
# print(personas[1])
print(f'inicio -> {personas}')

# Funciones
# append -> agrega un valor a la lista (se agrega al ultimo)
personas.append('Diego')
print(f'append -> {personas}')

# insert -> agrega un valor a la lista, le indicaremos en que indice o posición estara
personas.insert(0, "Eduardo")
print(f'insert -> {personas}')

# extend -> unir dos listas
personas_nuevas = ["Guiovany", "Henry", "Isabel", "Jean"]
personas.extend(personas_nuevas)
print(f'extend -> {personas}')

# remove -> eliminar un valor de la lista
personas.remove('Bruno')
print(f'remove -> {personas}')

# pop -> elimina el valor indicado por el indice
personas.pop(5)
print(f'pop -> {personas}')

# sort -> ordenar los valores de una lista
# reverse = False -> menor a mayor
# reverse = True -> mayor a menor
personas.sort(reverse=False)
print(f'sort -> {personas}')

# count -> retorna las veces que existe el mismo elemento en la lista
eduardo_contador = personas.count("Eduardo")
print(f'count -> {eduardo_contador}')

# len -> cuenta los elementos de una variable | length
print(f'Total de personas: {len(personas)}')
