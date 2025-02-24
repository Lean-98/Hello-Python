# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=29327

### Classes ###

# Definición

"""
 En Python, la palabra clave pass se utiliza como marcador de posición cuando no se necesita ninguna acción 
 o implementación específica en un bloque de código.
 Sirve para indicar que no se realizará ninguna operación dentro de ese bloque.
  Aunque no hace nada, su presencia es necesaria para mantener la sintaxis correcta del programa.
 Por ejemplo, se puede usar en la definición de funciones, clases, bucles y condicionales incompletos.
"""

"""
f en Python indica una f-string (formatted string), 
que permite insertar expresiones dentro de una cadena usando llaves {}
"""

class MyEmptyPerson:
    pass  # Para poder dejar la clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y propiedades privadas y públicas


class Person:
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name
    
    def set_name(self, nuevo_nombre):
         self.__name = nuevo_nombre

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("Brais", "Moure")
print(my_person.full_name)
print(my_person.get_name())
my_person.set_name('Leandro')
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de León (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 777
print(my_other_person.full_name)
