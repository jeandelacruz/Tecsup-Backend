# Tuplas (tuple) - Inmutable
personas = ("Jesus", "Miguel", "John")

# index -> retorna el indice del valor a buscar
indice_miguel = personas.index("Miguel")
print(f'index -> {indice_miguel}')

# count -> retorna las veces que existe un elemento
john_contador = personas.count("John")
print(f'count -> {john_contador}')

###################################################
personas_lista = list(personas)
personas_lista.append("Jorge")
print(type(personas_lista))
print(f'append -> {personas_lista}')

personas = tuple(personas_lista)
print(type(personas))
print(f'tupla -> {personas}')

# Investigación Adicional: Set y FrozenSet
