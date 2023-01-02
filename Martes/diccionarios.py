# Diccionario { key: value }
persona = {
    "nombre": "Brayan",
    "apellidos": "Acuña Ventosilla",
    "especialidades": [
        {
            "nombre": "Frontend"
        },
        {
            "nombre": "Backend"
        }
    ]
}

# persona.nombre
print(f'Nombre de la persona -> {persona["nombre"]}')
print(f'Segunda especialidad -> {persona["especialidades"][1]["nombre"]}')

# Agregar nuevo key (Clave)
persona["edad"] = 30
print(f'Diccionario nuevo -> {persona}')

# update -> actualizar un diccionario
persona.update({"hobbies": ["Jugar Play"]})
print(f'update -> {persona}')

# get -> busca la clave (key) en mención, y retorna su valor
# print(persona["nombres"])
# print(persona.get('nombres'))

# items -> una lista de tuplas (key, value)
print(f'items -> {persona.items()}')

# keys -> una lista con todas las claves
print(f'keys -> {persona.keys()}')

# values -> una lista de valores
print(f'values -> {persona.values()}')
