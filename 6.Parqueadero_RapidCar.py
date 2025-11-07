while True:
    print("\n¡Bienvenido al Parqueadero RapidCar!")
    horas = int(input("\nIngrese la cantidad de horas que desea estacionar (o 0 para salir): "))
    if horas == 0:
        print("\nGracias por usar el Parqueadero RapidCar. ¡Hasta luego!")
        break
    if horas < 0:
        print("Cantidad de horas inválida. Intente nuevamente.")
        continue  
    elif horas < 5:
        valor_hora = 2000
        total = horas * valor_hora
    elif horas > 5:
        valor_hora = 2000
        Multa = 5000
        total = (horas * valor_hora) + Multa
    else:
        print("\nCantidad de horas no válida. Intente nuevamente.")
        continue
    print("\n--- Resumen del estacionamiento ---")
    print(f"Horas estacionadas: {horas}")
    print(f"Valor por hora: ${valor_hora:,.0f}")
    if horas > 5:
        print(f"Multa por exceder 5 horas: ${Multa:,.0f}")
    print(f"Total a pagar: ${total:,.0f}")
    
    continuar = input("\n¿Desea realizar otro registro de estacionamiento? (s/n): ").strip().lower()
    if continuar != "s":    
        print("\nGracias por usar el Parqueadero RapidCar. ¡Hasta luego!")
        break