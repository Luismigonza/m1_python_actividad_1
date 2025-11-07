menu = 12000

while True:
    print("\n¡Bienvenido al Restaurante El Sabor Colombiano!")
    print("\nMenú del día - Precio fijo: $12.000")
    bebida = input("\n¿Desea agregar una bebida por $3.000 adicionales? (s/n): ").strip().lower()
    if bebida == 's':
        total = menu + 3000
        bebida_seleccionada = "con bebida"
    elif bebida == 'n':
        total = menu
        bebida_seleccionada = "sin bebida"
    else:
        print("\nOpción no válida. Intente nuevamente.")
        continue
    iva = total * 0.08
    total += iva
    print("\n--- Resumen de su pedido ---")
    print(f"Menú elegido: {bebida_seleccionada} - ${total:,.0f} (incluye IVA de ${iva:,.0f})")
    continuar = input("\n¿Desea realizar otro pedido? (s/n): ").strip().lower()
    