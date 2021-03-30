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

lista = []
primos = 0
contador = 0
nvect = int(input('Digite el tamaño del vector: '))
for i in range(1, nvect+1):
    numpri = int(input('Digite el numero a validar: '))
    lista.append(numpri)
    if numpri > 1:
        for j in range(2, numpri):
            restantes = (numpri % j)
            if restantes == 0:
                contador = contador + 1
        if contador == 0:
            primos = primos + 1
print(f'El vetor validado fue: {lista}')
print(f'La cantidad de elementos primos es: {primos}')

# Punto 3:
# A (Suma de vectores)

lista1 = []
lista2 = []

vect1 = int(input('Digite el tamaño para el vector 1: '))
vect2 = int(input('Digite el tamaño para el vector 2: '))

for i in range(1, vect1 + 1):
    n_vect1 = int(input(f'Digite los elementos # {i} para el vector 1: '))
    lista1.append(n_vect1)
    result1 = sum(lista1)

for i in range(1, vect2 + 1):
    n_vect2 = int(input(f'Digite los elementos # {i} para el vector 2: '))
    lista2.append(n_vect2)
    result2 = sum(lista2)
rtotal = result1 + result2
print(f'La suma del vector 1 {lista1} es: {result1}')
print(f'La suma del vector 2 {lista2} es: {result2}')
print(f'La suma de los dos vectores es: {rtotal}')

# Punto 3:
# B (Resta de vectores)

lista1 = []
lista2 = []

vect1 = int(input('Digite el tamaño para el vector 1: '))
vect2 = int(input('Digite el tamaño para el vector 2: '))

for i in range(1, vect1 + 1):
    n_vect1 = int(input(f'Digite los elementos # {i} para el vector 1: '))
    lista1.append(n_vect1)
    result1 = sum(lista1)

for i in range(1, vect2 + 1):
    n_vect2 = int(input(f'Digite los elementos # {i} para el vector 2: '))
    lista2.append(n_vect2)
    result2 = sum(lista2)
rtotal = result1 - result2
print(f'La suma del vector 1 {lista1} es: {result1}')
print(f'La suma del vector 2 {lista2} es: {result2}')
print(f'La resta de los dos vectores es: {rtotal}')
