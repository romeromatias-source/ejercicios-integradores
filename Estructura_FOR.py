#   ESTRUCTURA FOR - 11 Actividades en Python

def separador(titulo):
    print("\n" + "=" * 50)
    print(f"  {titulo}")
    print("=" * 50)


# Actividad 1: Números ascendentes del 1 al 10
separador("Actividad 1 - Números ascendentes del 1 al 10")

for i in range(1, 11):
    print(i)

# Actividad 2: Números descendentes del 10 al 1
separador("Actividad 2 - Números descendentes del 10 al 1")

for i in range(10, 0, -1):
    print(i)

# Actividad 3: Números desde 0 hasta el número ingresado
separador("Actividad 3 - Números desde 0 hasta N")

n = int(input("Ingresá un número: "))
for i in range(0, n + 1):
    print(i)

# Actividad 4: Tabla de multiplicar del número ingresado
separador("Actividad 4 - Tabla de multiplicar")

n = int(input("Ingresá un número para ver su tabla: "))
for i in range(0, 11):
    print(f"{n} x {i} = {n * i}")

# Actividad 5: Suma y promedio de hasta 10 números (0 termina)
separador("Actividad 5 - Suma y promedio (0 para terminar)")

suma = 0
cantidad = 0

for i in range(10):
    n = int(input(f"Número {i + 1} (0 para terminar): "))
    if n == 0:
        break
    suma += n
    cantidad += 1

if cantidad > 0:
    promedio = suma / cantidad
    print(f"\nSuma: {suma}")
    print(f"Cantidad de números: {cantidad}")
    print(f"Promedio: {promedio:.2f}")
else:
    print("No se ingresaron números.")

# Actividad 6: Múltiplos de 3 entre el 1 y el 100
separador("Actividad 6 - Múltiplos de 3 entre 1 y 100")

for i in range(1, 101):
    if i % 3 == 0:
        print(i)

# Actividad 7: Números pares del 1 al 50
separador("Actividad 7 - Números pares del 1 al 50")

for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# Actividad 8: Pirámide de números
separador("Actividad 8 - Pirámide de números")

n = int(input("Ingresá el tamaño de la pirámide: "))
for i in range(1, n + 1):
    fila = ""
    for j in range(1, i + 1):
        fila += str(j) + " "
    print(fila.strip())

# Actividad 9: Divisores de un número
separador("Actividad 9 - Divisores de un número")

n = int(input("Ingresá un número: "))
cantidad_divisores = 0

print(f"\nDivisores de {n}:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        cantidad_divisores += 1

print(f"\nCantidad de divisores encontrados: {cantidad_divisores}")

# Actividad 10: Determinar si un número es primo
separador("Actividad 10 - ¿Es primo?")

n = int(input("Ingresá un número: "))
es_primo = n > 1

for i in range(2, n):
    if n % i == 0:
        es_primo = False
        break

if es_primo:
    print(f"{n} ES un número primo.")
else:
    print(f"{n} NO es un número primo.")

# Actividad 11: Todos los primos entre 1 y N
separador("Actividad 11 - Números primos entre 1 y N")

n = int(input("Ingresá un número: "))
cantidad_primos = 0

print(f"\nNúmeros primos entre 1 y {n}:")
for i in range(2, n + 1):
    es_primo = True
    for j in range(2, i):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        print(i)
        cantidad_primos += 1

print(f"\nSe encontraron {cantidad_primos} números primos.")
print("¡Fin del programa!")