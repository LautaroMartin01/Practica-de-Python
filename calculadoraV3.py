def sumar (a, b):
    return a + b

def restar (a, b):
    return a - b

def dividir (a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    else:
        return a / b

def multiplicar (a, b):
    return a * b

def porcentaje (a, b):
    return a * b / 100

operaciones = {
    "+": sumar,
    "-" : restar,
    "*": multiplicar,
    "/": dividir,
    "%": porcentaje
}

def calculadora():
    try:
        num1 = float(input("Ingrese el primer numero: "))
    
    except ValueError: 
        print("El numero ingresado es invalido")
        while True:
            try:
                num1 = float(input("Ingrese el primer numero: "))
                break
            except ValueError:
                print("Ingrese un numero valido: ")

    while True:
        operacion = input("Ingrese la operacion a realizar (+, -, /, *, %, !? para finalizar: ")
        if operacion == "!?":
            print("Saliendo de la calculadora")
            break
    
        if operacion not in operaciones:
            print("La operacion no es valida ingrese nuevamente")
            continue
    
        try: 
            num2 = float(input("Ingrese el segundo numero: "))
            resultado = operaciones[operacion](num1, num2)
            num1 = resultado
            print(f"Resultado: {resultado}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("Error inesperado")



calculadora()
