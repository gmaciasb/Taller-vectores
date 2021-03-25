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


# Punto 2:
# A (Elementos pares)

cantidad = int(input('Digite el total de elementos que conforman el vector: '))
lista = []
pares = 0
for i in range(1, cantidad+1):
    elementos = int(input(f'Digite el elemento #{i}: '))
    if elementos % 2 == 0:
        pares = pares + 1
    lista.append(elementos)

print(f'Los elementos que conforman el vector son: {lista}')
print(f'La cantidad de elementos pares son: {pares}')

# Punto 2:
# B (Elementos impares)

cantidad = int(input('Digite el total de elementos que conforman el vector: '))
lista = []
impares = 0
for i in range(1, cantidad+1):
    elementos = int(input(f'Digite el elemento #{i}: '))
    if elementos % 2 != 0:
        impares = impares + 1
    lista.append(elementos)

print(f'Los elementos que conforman el vector son: {lista}')
print(f'La cantidad de elementos impares son: {impares}')

# Punto 2:
# C (Elementos primos)

num = int(input('Digite un elementos para el vector: '))
lista = []
contador = 0
primos = 0
if num > 1:
    for i in range(2, num):
        restantes = (num % i)
#        print("{} {} {}".format(num, i, restantes))
        if restantes == 0:
            contador = contador + 1
    if contador == 0:
        primos = primos + 1

# print(f'Los elementos que conforman el vector son: {lista}')
print(f'La cantidad de elementos primos son: {primos}')
