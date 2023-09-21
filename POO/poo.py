# Programación Orientada a Objetos
# Abstracción
# Clase: Control del Televisor
# encender
# apagar
# cambiar_canal
# bajar_volumen
# Nombre de la clase: PascalCase -> CamelCase

# {
#  "precio": "",
#  "tipo": "",
#  "color": ""
# }
# diccionario["precio"] -> diccionario.precio
class Mueble:
    # Sin constructor
    # precio = 0.00
    # tipo = ""
    # color = ""

    # Con constructor
    def __init__(self, tipo, precio=0.00, color=""):
        self.precio = precio
        self.tipo = tipo
        self.color = color

    # Metodo de instancia
    def indicarTipo(self):
        print(f'El tipo es {self.tipo}')


# Instancia de una clase
# sofa_cama = Mueble("Sofa Cama")
# sofa_cama.indicarTipo()
#
# silla = Mueble("Silla")
# silla.indicarTipo()

# Encapsulamiento
class Usuario:
    def __init__(self, usuario, contrasenia):
        self.usuario = usuario
        self.__contrasenia = contrasenia
        self.contrasenia = self.__encriptarContrasenia()
        self.__rol = ""

    # Primera forma
    # def __getRol(self):
    #     return self.__rol

    # def __setRol(self, valor):
    #     self.__rol = valor

    # rol_dos = property(__getRol, __setRol)

    # Segunda forma
    # Getter
    @property
    def rol_dos(self):
        return self.__rol

    # Setter
    @rol_dos.setter
    def rol_dos(self, valor):
        self.__rol = valor

    def __encriptarContrasenia(self):
        return f'%34%adsad${self.__contrasenia}··$·'


# pepito = Usuario("pepito", "123456")
# print(pepito.usuario)
# print(pepito.contrasenia)
# pepito.rol_dos = "Administrador"
# print(pepito.rol_dos)


# Herencia
# Clase Padre
class Mascota:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar(self):
        pass


# Clase Hija
class Perro(Mascota):
    def __init__(self, nombre, edad, duenio):
        # 1 Forma
        # self.nombre = nombre
        # self.edad = edad

        # 2 Forma
        super().__init__(nombre, edad)
        self.duenio = duenio

    def hablar(self):
        print('Guau!')


# Clase Hija
class Gato(Mascota):
    def hablar(self):
        print('Miau!')


dino = Perro("Dino", 3, "Jeancarlos")
print(dino.nombre)
print(dino.edad)
print(dino.duenio)
dino.hablar()

mimi = Gato("Mimi", 2)
print(mimi.nombre)
print(mimi.edad)
mimi.hablar()

# Polimorfismo
