num1 =  int(input("Ingrese el primer numero que quiere utilizar para realizar la operacion: "))
resultado = 0
num2 = 0

while True:
    operacion = input("Ingrese el simbolo de la operacion a realizar (!? para finalizar): ")
    if operacion == "+":

        num2 = int(input ("Ingrese el numero a sumar: "))
        resultado = num1 + num2
        print(resultado)

    elif operacion == "-":

        num2 = int(input ("Ingrese el numero a restar: "))
        resultado = num1 - num2
        print(resultado)

    elif operacion == "*":

        num2 = int(input ("Ingrese el numero a multiplicar: "))
        resultado = num1 * num2
        print(resultado)

    elif operacion == "/":

        num2 = int(input ("Ingrese el numero a dividir: "))
        resultado = num1 / num2
        print(int(resultado)) 
        # Para que no salga con coma

    elif operacion == "%":

        num2 = int(input ("Ingrese el porcentaje del numero: "))
        resultado = num1 * num2/100
        print(resultado)

    elif operacion == "!?":
        break

    num1 = resultado