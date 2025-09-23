#                                               Suma

numeros = [1, 2, 3, 4, 5, 6, 8]
sumaTotal = 0
sumaTotal1 = sum(numeros)
print(sumaTotal1)
sumaTotal2 = 0

for i in range(7):
    sumaTotal = numeros[i] + sumaTotal
print(sumaTotal)


for numero in numeros:
    sumaTotal2 += numero
print(sumaTotal2)

# Hice 3 opciones que se ocurrieron para el problema

#                                               Promedio

for cantNumeros in numeros:
    cantNumeros += 1

promedio = (sumaTotal / cantNumeros)

print(promedio)

#                                               Minimo

minimo = min(numeros)
print (minimo)

numMinimo = numeros[0]

for numero in numeros:
    if numero < numMinimo:
        numMinimo = numero

print(numMinimo)

# Hice 2 opciones que se ocurrieron para el problema

#                                               Maximo

maximo = max(numeros)
print(maximo)

numMaximo = numeros[0]

for numero in numeros:
    if numero > numMaximo:
        numMaximo = numero

print(numMaximo)