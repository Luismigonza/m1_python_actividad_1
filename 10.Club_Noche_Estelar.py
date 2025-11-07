while True:
    print("\n¡Bienvenido al CLub Noche Estelar!")
    print("\nPara poder ingresar, Compartanos los siguientes datos:")
    edad = int(input("\nIngrese su edad (o 0 para salir): "))
    documento = input("\n¿Tiene documento de identidad? (s/n): ").strip().lower()
    if documento != 's':
        print("\nLo siento, es obligatorio presentar documento de identidad para ingresar.")
        continue
    if edad == 0:
        print("\nGracias por su visita. ¡Hasta luego!")
        break
    elif edad >= 18:
        print("\n¡Bienvenido al Club Noche Estelar! Disfrute de su noche.")
    elif edad < 18:
        print("\nEntrada Denegada.")
    else:
        print("\nEdad no válida. Intente nuevamente.")
        continue
    continuar = input("\n¿Desea verificar otra entrada? (s/n): ").strip().lower()
    if continuar != "s":    
        print("\nGracias por su visita. ¡Hasta luego!")
        break