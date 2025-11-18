precio_pan = 300 

while True:
    cantidad = int(input("\nIngrese la cantidad de panes que desea comprar (o 0 para salir): "))

    if cantidad == 0:
        print("\nGracias por su compra. ¡Vuelva pronto!")
        break
    if cantidad < 0:
        print("El valor ingrado no es valido, Vuelva a intentar")
        continue

    if cantidad < 0:
        print("Cantidad inválida. Intente nuevamente.")
        continue  # Vuelve al inicio del ciclo

    subtotal = cantidad * precio_pan

    if cantidad > 50:
        descuento = 0.20
    elif cantidad > 20:
        descuento = 0.10
    else:
        descuento = 0.0

    total = subtotal * (1 - descuento)

    print("\n--- Resumen de la compra ---")
    print(f"Cantidad de panes: {cantidad}")
    print(f"Precio unitario: ${precio_pan}")
    print(f"Descuento aplicado: {descuento * 100}%")
    print(f"Total a pagar: ${total:,.0f}")

    continuar = input("\n¿Desea realizar otra compra? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nGracias por su compra. ¡Hasta luego!")
        break
    


#prueba cambio
#cambio con cuenta iniciada