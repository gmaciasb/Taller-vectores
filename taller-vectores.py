# Gabriel Macias
# Taller 2do corte - vectores

# Punto 1:
# C (El Mayor elemento)

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
