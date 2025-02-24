# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=34583

### Modules ###
"""
 Un módulo es un archivo que contiene un conjunto de códigos o un conjunto de funciones
 que se pueden incluir en una aplicación. 
 Un módulo puede ser un archivo que contenga una única variable, una función o una gran base de código.
"""


from math import pi as PI_VALUE
import math
from my_module import sumValue, printValue
import my_module

my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python!")


sumValue(5, 3, 1)
printValue("Hola python")


print(math.pi)
print(math.pow(2, 8))


print(PI_VALUE)
