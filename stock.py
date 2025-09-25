def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

productos = [
    {"nombre": "Coca-Cola", "stock": 200},
    {"nombre": "Fanta", "stock": 200}
    ]

while True:

    print("1- Agregar producto")
    print("2- Ver productos")
    print("3- Venta de producto")
    print("4- Comprar de producto")

    opcion = input("Elija la operacion a realizar: ")

    if opcion == "1":
        nombreProducto = input("Nombre de producto: ")
        stockProducto = int(input("Cantidad a agregar: "))
        productoEncontrado = False
        
        for producto in productos:
            if producto["nombre"].lower() == nombreProducto.lower():
                producto["stock"] = sumar(producto["stock"], stockProducto)
                print(f"El stock de {nombreProducto} a sido actulizado y ahora es de {producto["stock"]} ")
                productoEncontrado = True
                break
        if not productoEncontrado:
            productos.append({"nombre" : nombreProducto, "stock" : stockProducto})
            print("El producto a sido agregado exitosamente")

    elif opcion == "2":
        for i, producto in enumerate(productos):
            print(f"{i}.{producto}")

    elif opcion =="3":
        nombreProductoVendido = input("Ingrese el nombre del producto vendido: ")
        venta = None
        for producto in productos:
            if producto["nombre"].lower() == nombreProductoVendido.lower():
                venta = nombreProductoVendido
                break 
        if venta:
            try:
                stockVendido = int(input("Ingrese la cantidad que se vendio: "))
                if stockVendido > producto["stock"]:
                    print("No se puede vender mas de lo que se tiene")
                else:    
                    producto["stock"] = restar(producto["stock"], stockVendido)
                    print(f"El nuevo stock del producto {venta} es de {producto["stock"]} productos")
            except ValueError:
                print("Error al ingresar la cantidad")
        else: print("El producto no fue encontrado")
    elif opcion == "4":
        nombreProductoComprado = input("Ingrese el nombre del producto comprado: ")
        compra = None
        for producto in productos:
            if producto["nombre"].lower() == nombreProductoComprado.lower():
                compra = nombreProductoComprado
                break
        if compra:
            try:
                stockProductoComprado = int(input("Ingrese la cantidad comprada: "))
                if stockProductoComprado <= 0:
                    print("Error el minimo de compra es 1 unidad")
                else:
                    producto["stock"] = sumar(producto["stock"], stockProductoComprado)
                    print(f"El nuevo stock de producto {nombreProductoComprado} es de {producto["stock"]} unidades")
            except ValueError:
                print("Error al ingresar la cantidad")
        else:
            print("El producto no fue encontrado")
    else:
        print("EL numero ingresado es erroneo")
            
            
            
        


