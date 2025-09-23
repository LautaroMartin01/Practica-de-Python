contador = 1

while contador <= 100:
    print(contador)
    if (contador % 3 == 0):
        print("Frizz")
    if (contador % 5 == 0):
        print("Buzz")
    if (contador % 3 == 0 and contador % 5 == 0):
        print("FrizzBuzz")
    contador += 1
    