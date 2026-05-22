# SISTEMA DE VENTAS - CADENA DE SUPERMERCADOS

TIPOS_PRODUCTO = ["alimento", "limpieza", "perfumeria"]
FORMAS_PAGO    = ["efectivo", "tarjeta", "transferencia"]
TOTAL_VENTAS   = 25

# funciones de validación 

def pedir_tipo_producto():
    while True:
        print("Tipos de producto: alimento / limpieza / perfumeria")
        valor = input("Tipo de producto: ").strip().lower()
        if valor in TIPOS_PRODUCTO:
            return valor
        print("Error: tipo de producto inválido.")

def pedir_cantidad():
    while True:
        try:
            valor = int(input("Cantidad de unidades (1-20): "))
            if 1 <= valor <= 20:
                return valor
            print("Error: la cantidad debe estar entre 1 y 20.")
        except ValueError:
            print("Error: ingrese un número entero.")

def pedir_precio():
    while True:
        try:
            valor = float(input("Precio unitario (mayor a 0): "))
            if valor > 0:
                return valor
            print("Error: el precio debe ser mayor a 0.")
        except ValueError:
            print("Error: ingrese un número válido.")

def pedir_forma_pago():
    while True:
        print("Formas de pago: efectivo / tarjeta / transferencia")
        valor = input("Forma de pago: ").strip().lower()
        if valor in FORMAS_PAGO:
            return valor
        print("Error: forma de pago inválida.")

# registro de ventas 

ventas = []
total_unidades = 0

print("   REGISTRO DE VENTAS DIARIAS - SUPERMERCADO")

for i in range(1, TOTAL_VENTAS + 1):
    print(f"\n--- Venta N° {i} ---")

    tipo     = pedir_tipo_producto()
    cantidad = pedir_cantidad()
    precio   = pedir_precio()
    pago     = pedir_forma_pago()

    subtotal = cantidad * precio

    # descuento del 5 % por pago en efectivo
    descuento_efectivo = 0
    if pago == "efectivo":
        descuento_efectivo = subtotal * 0.05
    subtotal_final = subtotal - descuento_efectivo

    total_unidades += cantidad

    ventas.append({
        "tipo":               tipo,
        "cantidad":           cantidad,
        "precio":             precio,
        "pago":               pago,
        "subtotal":           subtotal,
        "descuento_efectivo": descuento_efectivo,
        "subtotal_final":     subtotal_final,
    })

# cálculos finales 

# 1. importe total bruto (sin descuentos)
total_bruto = sum(v["subtotal"] for v in ventas)

# descuento global por volumen
if total_unidades > 400:
    porcentaje_volumen = 0.20
elif total_unidades > 200:
    porcentaje_volumen = 0.10
else:
    porcentaje_volumen = 0.0

# 2. importe total final con todos los descuentos
suma_subtotales_con_efectivo = sum(v["subtotal_final"] for v in ventas)
descuento_volumen = suma_subtotales_con_efectivo * porcentaje_volumen
total_final = suma_subtotales_con_efectivo - descuento_volumen

# 3. venta más cara pagada con tarjeta
ventas_tarjeta = [v for v in ventas if v["pago"] == "tarjeta"]
if ventas_tarjeta:
    venta_cara_tarjeta = max(ventas_tarjeta, key=lambda v: v["subtotal_final"]) #RECORDAR lambda es sin necesidad de definir con def
else:
    venta_cara_tarjeta = None

# 4. promedio de precio unitario
promedio_precio = sum(v["precio"] for v in ventas) / len(ventas)

# 5. forma de pago más utilizada
conteo_pago = {forma: 0 for forma in FORMAS_PAGO}
for v in ventas:
    conteo_pago[v["pago"]] += 1
forma_mas_usada  = max(conteo_pago, key=conteo_pago.get)
cantidad_mas_usada = conteo_pago[forma_mas_usada]

# resultados 

print("\n" + "=" * 50)
print("              RESULTADOS DEL DÍA")
print("=" * 50)

print(f"\nTotal de unidades vendidas : {total_unidades}")

print(f"\n1. Importe total bruto      : ${total_bruto:,.2f}")

if porcentaje_volumen > 0:
    print(f"   Descuento por volumen    : {int(porcentaje_volumen * 100)}%"
          f"  (> {'200' if porcentaje_volumen == 0.10 else '400'} unidades)")
else:
    print("   Sin descuento por volumen (< 200 unidades)")

print(f"\n2. Importe total final       : ${total_final:,.2f}")

print("\n3. Venta más cara con tarjeta:")
if venta_cara_tarjeta:
    print(f"   Producto  : {venta_cara_tarjeta['tipo']}")
    print(f"   Cantidad  : {venta_cara_tarjeta['cantidad']} unidades")
    print(f"   Precio    : ${venta_cara_tarjeta['precio']:,.2f}")
    print(f"   Subtotal  : ${venta_cara_tarjeta['subtotal_final']:,.2f}")
else:
    print("   No hubo ventas pagadas con tarjeta.")

print(f"\n4. Promedio precio unitario  : ${promedio_precio:,.2f}")

print(f"\n5. Forma de pago más usada   : {forma_mas_usada.capitalize()}"
      f"  ({cantidad_mas_usada} veces)")

print(f"\n   Detalle de formas de pago:")
for forma, cant in conteo_pago.items():
    print(f"   - {forma.capitalize():15s}: {cant} venta/s")

print("\n" + "=" * 50)