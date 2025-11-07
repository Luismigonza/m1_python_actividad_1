libro = 25000

while True:
    print("Bienvenido a la Librería El Saber")
    print("\nPara continuar con su Compra, Responda las siguientes preguntas:")
    estudiante = input("\n¿Es usted estudiante? (s/n): ").strip().lower()
    Cupon = input("\nIngrese el codigo de Cupon que posee (o 'ninguno' si no tiene): ").strip()
    
    if estudiante == 'n' and Cupon == 'ninguno':
        descuento = 0.0
    elif estudiante == 's' and Cupon == 'ninguno':
        descuento = 0.15
    elif estudiante == 'n' and Cupon == 'LIBRO10':
        descuento = 0.0
    elif estudiante == 's' and Cupon == 'LIBRO10':
        descuento = 0.25
    elif estudiante == 'n' and Cupon == '':
        descuento = 0.0
    elif estudiante == 's' and Cupon == '':
        descuento = 0.0
    else:
        print("\nDato no Valido. Intente nuevamente.")
        continue
    
    total = libro * (1 - descuento)
    
    print("\n--- Resumen de la compra ---")
    print(f"Precio del libro: ${libro}")
    print(f"Descuento aplicado: {descuento * 100}%")
    print(f"Total a pagar: ${total:,.0f}")
    
    continuar = input("\n¿Desea realizar otra compra? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nGracias por su compra. ¡Hasta luego!")
        break
    
    