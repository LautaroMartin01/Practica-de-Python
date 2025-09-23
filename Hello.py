print ("Hola Python")

nombre = "Lautaro"
edad = 23
altura = 1.70
es_programador = True

print (nombre, edad, altura, es_programador)

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(es_programador))

if edad >= 18: 
    print ("Sos mayor")
else: 
    print("Sos menor")

for i in range(5):
    print(i)

contador = 0
while contador <= 5:
    print(contador)
    contador += 1

def saludar(nombre):
    return f"Hola {nombre}!"

print (saludar("Luca"))

numeros = [1, 2, 3, 4, 5]
print (numeros[1])

persona = {"nombre": "Lautaro", "edad": 23}
print(persona["nombre"])

coordenas = (10.5, 20.3)
print(coordenas[1])

colores = {"rojo", "verde", "azul"}
print("rojo" in colores)




