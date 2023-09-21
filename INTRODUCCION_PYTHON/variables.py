# Solo pueden ser nombrados con letras, no alfanumericos, ni numericos.
## Formato: Snakecase
# nombre_de_variable
# Hay valores o nombres reservados, tener precaución
# main -> jamas en su vida

# Tipo de Datos
# String -> Variables de texto (str)

# Comillas simples y comillas dobles (ambas)
nombre = "Jeancarlos"
apellidos = 'De la cruz'
texto_largo = """
Buenos noches,
    La carta redactada....
    .......
"""
texto_largo_en_linea = (
    "Hola, como estas? "
    "es tarde por alla? "
    "abrigate :) "
    "te me cuidas :)"
)

# Operador de salida -> console.log <-> print
# print(nombre, type(nombre))
# print(texto_largo, type(texto_largo))
# print(texto_largo_en_linea, type(texto_largo_en_linea))

# Numericos -> Enteros (int), Decimales y Flotantes (float)
enteros = 5
decimales = 10.20

# Booleanos -> true (1) y false (0)
verdadero = True
falso = False

# Valor Nulo -> null
variable_nulo = None

# Concatenación
#print(nombre + " " + apellidos)
#print(nombre, apellidos)
# Template Syntax -> `${}`
#print(f"{nombre} {apellidos}")

# Tipado Dinamico
# print(type(nombre))
#nombre = 1500
# print(type(nombre))

# Asignación Multiple (Se debe tener en cuenta en tener las mismas variables con sus datos)
#persona = "Bruno"
#edad = 22
persona, edad = "Bruno", 22
print(persona)
print(edad)
