while True:
    edad = int(input("!Bienvenido a Cine La Estrella¡ Ingrese su edad Por favor (o 0 para salir): "))

    if edad == 0:
        print("Gracias por visitarnos. ¡Hasta luego!")
        break
    if edad < 0:
        print("La edad ingresada no es valida, Vuelve a ingresar")
        continue

    if edad <= 0:
        print("Edad inválida. Intente nuevamente.")
        continue
    elif edad < 5:
        precio_entrada = "Gratis"
    elif edad >=5 and  edad <= 11:
        precio_entrada = 5000
    elif edad >= 12 and edad <= 59:
        precio_entrada = 8000
    else:  # edad >= 60
        precio_entrada = 4000 

    print("\n--- Resumen de la compra ---")
    print(f"Edad del cliente: {edad}")
    print(f"Precio de la entrada: {precio_entrada:,.0f}")
    if precio_entrada == 4000:
        print("¡Disfruta tu descuento para adultos mayores!")

    continuar = input("\n¿Desea procesar otra entrada? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nGracias por visitarnos. ¡Hasta luego!")
        break