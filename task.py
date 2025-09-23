tareas = []

#Creamos un array vacio para guardar las tareas

while True:
    
    print("Ingrese 1 si quiere agregar una tarea.")
    print("Ingrese 2 si quiere ver las tareas.")
    print("Ingrese 3 si quiere salir.")

    #Le damos al usuario una serie de opciones para que el elija cual es la mas adecuada para su necesidad

    opcion = input("Ingrese el numero: ")

    if opcion == "1":
        descripcion = input("Describa la tarea a realizar: ")
        tareas.append(descripcion)
        print("Tarea agregada correctamente")

        # Si el usuario ingreso el numero 1, entonces se le pide que describa la tarea y esta se guarda en el array de tareas en la primera posicion

        masTareas = input ("Desea agregar mas tareas SI o NO ")
        
        # Se le pregunta al usuario si quiere agregas mas tareas

        if masTareas == "SI":
            canTareas  = int(input("Ingrese el numero de tareas a ingresar: "))
            
            # Si la respuesta del usuario es si entonces se le procede a preguntar la cantidad a agregar y se pone un int ya que el usuario va a ingresar un numero en formato texto y esto lo que hace es convertirlo a formato numerico para luego utilizarlo en el for
            
            for i in range(canTareas):
                descripcionTareas = input ("Describa la tarea a realizar: ")
                tareas.append(descripcionTareas)
                print("Tarea agregada correctamente")

            # Una vez que el usuario ingreso la cantidad de tareas que quiere agregar se procede a hacer un for para que este iterer entre las posiciones del array y vaya guardando en las posiciones de memoria las descripciones que el usuario ingresa, mediante el .append

    elif opcion == "2":
        if not tareas:
            print("No hay tareas disponibles")

        # Si el usuario ingresa el numero 2 y no hay ninguna tarea asignada lo que sucese es que se muestra un mensaje

        else:
            print("Tus tareas")
            for i, tareas in enumerate(tareas, 1):
                print(f"{i}.{tareas}")

        # Si el usuario ingresa el numero 2 y hay tareas asignadas lo que sucesde es que se entra en un bucle for en donde se utiliza la i para iterar (las vueltas) y el array de tareas ya que en este es donde estan guaradas las tareas para luego mostrarlas. Se utiliza el enumerate ya que nos da el elemento de la lista y al enumeracion que en este caso arranca en 1 y luego se imprime en pantalla una abajo de la otra

    elif opcion == "3":
        break
    else: print ("La opcion no es valida vuelva a intentar")
        

