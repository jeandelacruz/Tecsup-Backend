# IF, ELSE, ELSEIF
# if(condicion) { ... }

numero = int(input("Ingrese un número: "))

# Si la variable numero es igual a 10, que me muestre el mensaje "Cumple condición"
# Si es menor a 10, que muestre el mensaje "Cumple condición menor"
# Y si es diferente a los dos casos, que muestre "No cumple la condición"

# if numero == 10:
#     print('Cumple condición')
# elif numero < 10:
#     print('Cumple condición menor')
# else:
#     print('No cumple condición')

# Operador ternario -> condicion ? true : false
print('Verdadero' if numero == 10 else 'Falso')
