import pdb  

total_acumulado = 0.0
cantidad_transacciones = 0
historial_ventas = []  

activo = True
while activo:
    print("=== SISTEMA DE CAJA REGISTRADORA OXXO ===")
    print("1. Registrar venta de producto")
    print("2. Ver resumen y acumulado")
    print("3. Salir del sistema")
    
    opcion = input("Selecciona una opción (1-3): ")
    
    if opcion == "1":
        print("\n--- Registro de Venta ---")
        precio_str = input("Ingresa el precio unitario: ")
        cantidad_str = input("Ingresa la cantidad de piezas: ")
        
        precio = float(precio_str)
        cantidad = int(cantidad_str)
        
        subtotal = precio * cantidad
        
        if cantidad >= 10:
            descuento = subtotal * 0.10
            total_venta = subtotal - descuento
            print("¡Aplica descuento del 10%!")
        else:
            total_venta = subtotal
            print("No aplica descuento.")
        
        total_acumulado += total_venta
        cantidad_transacciones += 1
        historial_ventas.append(total_venta)
        
        print("Total a pagar por esta venta: $", round(total_venta, 2))
        
    elif opcion == "2":
        print("\n--- Resumen de Operaciones ---")
        print("Total de ventas realizadas:", cantidad_transacciones)
        print("Monto total acumulado en caja: $", round(total_acumulado, 2))
        
        if len(historial_ventas) > 0:
            print("\nDesglose de los montos cobrados:")
            for i in range(len(historial_ventas)):
                print("  Venta #", i + 1, ": $", round(historial_ventas[i], 2))
        else:
            print("Aún no hay ventas registradas.")
            
    elif opcion == "3":
        print("\nCerrando sistema. ¡Hasta luego!")
        activo = False  
    else:
        print("Opción inválida. Ingresa 1, 2 o 3.")
        
    pdb.set_trace()