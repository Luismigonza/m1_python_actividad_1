while True:
    print("\n¡Bienvenido a la Empresa TecnoPlus!")
    nota_tecnica = float(input("\nIngrese la nota de la prueba técnica (0.0 - 5.0): "))
    nota_logica = float(input("Ingrese la nota de la prueba lógica (0.0 - 5.0): "))

    nota_final = (nota_tecnica * 0.7) + (nota_logica * 0.3) 

    if nota_tecnica < 0.0 or nota_tecnica > 5.0 or nota_logica < 0.0 or nota_logica > 5.0:
        print("\nNotas inválidas. Intente nuevamente.")
        continue
    elif nota_final >= 3:
        resultado = "Aprobado"
    elif nota_final >= 2 and nota_final < 3:
        resultado = "Revisión"
    elif nota_final < 2:
        resultado = "Reprobado"
    else:
        resultado = "Rechazado"
    print("\n--- Resultado de la evaluación ---")
    print(f"Nota Técnica: {nota_tecnica}")
    print(f"Nota Lógica: {nota_logica}")
    print(f"Nota Final: {nota_final:.2f}")
    print(f"Resultado: {resultado}")
    
    continuar = input("\n¿Desea evaluar otro candidato? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nGracias por usar el sistema de evaluación de TecnoPlus. ¡Hasta luego!")
        break