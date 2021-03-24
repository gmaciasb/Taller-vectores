# Gabriel Macias
# Taller 2do corte - vectores

# Punto 1:
# C (El Mayor elemento)
import numpy as np

c_numeros = int(input('Digite la cantidad de numeros para el vector: '))
contenedor = []
mayor = 0
i = 1

while (c_numeros > 0):
    nums = int(input(f'Digite el numero {i} para el vector: '))
    contenedor.append(nums)
    i = i + 1
    c_numeros = c_numeros - 1

mayor = max(contenedor)

print(f'Los elementos del vector son: {contenedor}')
print(f'El elemento mayor es: {mayor}')

# Punto 1:
# d (El menor elemento)

c_numeros = int(input('Digite la cantidad de numeros para el vector: '))
contenedor = []
menor = 0
i = 1

while (c_numeros > 0):
    nums = int(input(f'Digite el numero {i} para el vector: '))
    contenedor.append(nums)
    i = i + 1
    c_numeros = c_numeros - 1

menor = min(contenedor)

print(f'Los elementos del vector son: {contenedor}')
print(f'El elemento menor es: {menor}')

# Punto 1:
# a (La sumatoria)

c_numeros = int(input('Digite la cantidad de numeros para el vector: '))
contenedor = []
suma = 0
i = 1

while (c_numeros > 0):
    nums = int(input(f'Digite el numero {i} para el vector: '))
    contenedor.append(nums)
    i = i + 1
    c_numeros = c_numeros - 1

suma = sum(contenedor)

print(f'Los elementos del vector son: {contenedor}')
print(f'La sumatoria de los elementos es: {suma}')

# Punto 1:
# b (La productoria)

c_numeros = int(input('Digite la cantidad de numeros para el vector: '))
contenedor = []
producto = 0
i = 1

while (c_numeros > 0):
    nums = int(input(f'Digite el numero {i} para el vector: '))
    contenedor.append(nums)
    i = i + 1
    c_numeros = c_numeros - 1

producto = np.prod(contenedor)

print(f'Los elementos del vector son: {contenedor}')
print(f'La productoria de los elementos es: {producto}')
