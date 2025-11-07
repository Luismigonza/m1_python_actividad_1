while True:
    dias = int(input("\n¡Bienvenido al Gimnasio Solo Leveling! Ingrese la cantidad de días que entreno esta semana (o 0 para salir): "))

    if dias == 0:
        print("\nNo aflojes, tú puedes mejorar")
        print("¡Gracias por entrenar con nosotros! ¡Hasta luego!")
        break

    if dias >= 4:
        print("\n¡Excelente disciplina!")
        print("\nGanaste un Punto de Energía")
    elif dias == 2 or dias == 3:
        print("\nBien, pero puedes dar más de ti.")
    elif dias == 0 or dias == 1:
        print("\nNo aflojes, tú puedes mejorar")

    continuar = input("\n¿Desea registrar otra semana? (s/n): ").strip().lower()
    if continuar != "s":
        print("\n¡Gracias por entrenar con nosotros! ¡Hasta luego!")
        break