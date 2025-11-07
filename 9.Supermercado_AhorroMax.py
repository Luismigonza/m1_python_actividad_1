precio_unitario = 2000

while True:
    print("\n¡Bienvenido a la Empresa TecnoPlus!")
    print("\nEl precio fijo de cada producto es de $2.000")
    unidades = int(input("\nIngrese la cantidad de unidades que desea comprar (o 0 para salir): "))
    if unidades == 0:
        print("\nGracias por comprar en Supermercado AhorroMax. ¡Hasta luego!")
        break
    elif unidades < 0:
        print("\nCantidad inválida. Intente nuevamente.")
        continue
    elif unidades == 30:
        descuento = 0.15
    elif unidades == 10:
        descuento = 0.05
    else:
        descuento = 0.0
    subtotal = unidades * precio_unitario
    total = subtotal * (1 - descuento)
    
    if total < 50000:
        costo_envio = 5000
    else:
        costo_envio = 0
    total += costo_envio
    print("\n--- Resumen de la compra ---")
    print(f"Unidades compradas: {unidades}")
    print(f"Precio unitario: ${precio_unitario:,.0f}")
    print(f"Descuento aplicado: {descuento * 100}%")
    print(f"Costo de envío: ${costo_envio}")
    print(f"Total a pagar: ${total:,.0f}")
    
    continuar = input("\n¿Desea realizar otra compra? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nGracias por comprar en Supermercado AhorroMax. ¡Hasta luego!")
        break
