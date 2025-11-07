while True:
    print("\n¡Bienvenido a la Heladería Frosty!")
    print("\nSabores disponibles:")
    print("\n1. Chocolate - $4.000")
    print("\n2. Vainilla - $3.500")
    
    sabor = int(input("\nIngrese el número del sabor que desea (o 0 para salir): "))

    if sabor == 0:
        print("\nGracias por visitar Heladería Frosty. ¡Vuelva pronto!")
        break
    elif sabor not in [1, 2]:
        print("\nSabor no Disponible. Intente nuevamente.")
        continue  
    elif sabor == 1:
        precio = 4000
        nombre_sabor = "Chocolate"
    else:
        precio = 3500
        nombre_sabor = "Vainilla"

    print("\nTenemos los siguientes topping:")
    print("\n1. Chispas de chocolate - $1.000")
    print("\n2. Frutas frescas - $1.000")
    topping = int(input("\nIngrese el número del topping que desea (o 0 para sin topping): "))
    if topping == 0:
        precio_topping = 0
        nombre_topping = "Sin topping"
    elif topping in [1, 2]:
        precio_topping = 1000
        nombre_topping = "Chispas de chocolate" if topping == 1 else "Frutas frescas"
    else:
        print("\nTopping no Disponible. Intente nuevamente.")
        continue
    total = precio + precio_topping
    print("\n--- Resumen de su pedido ---")
    print(f"Sabor elegido: {nombre_sabor} - ${precio}")
    print(f"Topping elegido: {nombre_topping} - ${precio_topping}")
    print(f"Total a pagar: ${total}")

    continuar = input("\n¿Desea realizar otro pedido? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nGracias por visitar Heladería Frosty. ¡Hasta luego!")
        break
    