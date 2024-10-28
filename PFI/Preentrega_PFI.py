product_list = []
product_list.clear() #libero espacio en memoria (la lista es mutable)

while True:
    print("Menu")
    print("1 - Agregar producto")
    print("2 - Listar productos")
    print("3 - Salir")
    option = input("\nIngrese la opción que desea: ")

    if option == "1":
        element= []
        #Alta de producto
        product_name = input ("Ingrese el nombre del producto: ")
        product_quantity = int(input("Ingrese la cantidad disponible: ")) 
        element.append(product_name)
        element.append(product_quantity)
        product_list.append(element)

    elif option == "2":
        #Listar productos
        print("Lista de Productos")
        index=0
        while index < len(product_list):            
            print(f"Producto {product_list[index][0]}: cantidad {product_list[index][1]}")
            index +=1

    elif option == "3":
        break
    
    else:
        print("Ud. ha ingresado una opción inválida, intente nuevamente")   