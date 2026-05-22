#   TORNEO DE PING-PONG — Tabla de Posiciones / Estadísticas

# Constantes de validación
TIPOS_SAQUE   = ("plano", "liftado", "cortado")
CATEGORIAS    = ("elite", "experto", "avanzado")
MAX_PUNTOS    = 60
MAX_PARTIDOS  = 35

# Funciones de validación
def validar_edad(valor: str) -> int:
    """Devuelve la edad como entero o lanza ValueError."""
    edad = int(valor)
    if edad <= 0:
        raise ValueError("La edad debe ser un número entero positivo.")
    return edad

def validar_entero_positivo(valor: str, campo: str, maximo: int) -> int:
    """Valida un campo entero positivo con cota superior."""
    numero = int(valor)
    if numero < 0:
        raise ValueError(f"{campo} debe ser un número entero positivo.")
    if numero > maximo:
        raise ValueError(f"{campo} no puede superar {maximo}.")
    return numero

def validar_opcion(valor: str, opciones: tuple, campo: str) -> str:
    """Valida que el valor esté entre las opciones permitidas."""
    valor = valor.strip().lower()
    if valor not in opciones:
        raise ValueError(
            f"{campo} inválido. Opciones: {', '.join(opciones)}."
        )
    return valor

# Carga de datos
def ingresar_jugador() -> dict:
    """
    Solicita y valida los datos de un jugador.
    Retorna un diccionario con sus atributos.
    """
    print("\n--- Datos del jugador ---")

    # Nombre
    nombre = input("Nombre del jugador: ").strip()
    while not nombre:
        print("  ✗ El nombre no puede estar vacío.")
        nombre = input("Nombre del jugador: ").strip()

    # Edad
    while True:
        try:
            edad = validar_edad(input("Edad: "))
            break
        except ValueError as e:
            print(f"  ✗ {e}")

    # Puntos
    while True:
        try:
            puntos = validar_entero_positivo(
                input(f"Cantidad de puntos (0-{MAX_PUNTOS}): "),
                "Puntos", MAX_PUNTOS
            )
            break
        except ValueError as e:
            print(f"  ✗ {e}")

    # Partidos ganados
    while True:
        try:
            partidos = validar_entero_positivo(
                input(f"Partidos ganados (0-{MAX_PARTIDOS}): "),
                "Partidos ganados", MAX_PARTIDOS
            )
            break
        except ValueError as e:
            print(f"  ✗ {e}")

    # Tipo de saque
    while True:
        try:
            saque = validar_opcion(
                input(f"Tipo de saque {TIPOS_SAQUE}: "),
                TIPOS_SAQUE, "Tipo de saque"
            )
            break
        except ValueError as e:
            print(f"  ✗ {e}")

    # Categoría
    while True:
        try:
            categoria = validar_opcion(
                input(f"Categoría {CATEGORIAS}: "),
                CATEGORIAS, "Categoría"
            )
            break
        except ValueError as e:
            print(f"  ✗ {e}")

    return {
        "nombre":   nombre,
        "edad":     edad,
        "puntos":   puntos,
        "partidos": partidos,
        "saque":    saque,
        "categoria": categoria,
    }

def cargar_jugadores() -> list:
    """Carga todos los jugadores hasta que el usuario decida detenerse."""
    jugadores = []
    print("=" * 50)
    print("  CARGA DE JUGADORES — Torneo de Ping-Pong")
    print("=" * 50)
    while True:
        jugador = ingresar_jugador()
        jugadores.append(jugador)
        print(f"Jugador '{jugador['nombre']}' cargado correctamente.")
        continuar = input("\n¿Cargar otro jugador? (s/n): ").strip().lower()
        if continuar != "s":
            break
    return jugadores

# Estadísticas — Tema A
def estadistica_a1(jugadores: list) -> int:
    """
    A1: Cantidad de jugadores de categoría 'elite' con saque 'plano'
        cuya edad esté entre 19 y 25 años inclusive.
    """
    return sum(
        1 for j in jugadores
        if j["categoria"] == "elite"
        and j["saque"] == "plano"
        and 19 <= j["edad"] <= 25
    )

def estadistica_a2(jugadores: list) -> dict | None:
    """
    A2: Nombre y Categoría del jugador de menor edad con más de 50 puntos.
    """
    candidatos = [j for j in jugadores if j["puntos"] > 50]
    if not candidatos:
        return None
    return min(candidatos, key=lambda j: j["edad"])

def estadistica_a3(jugadores: list) -> float:
    """
    A3: Porcentaje de jugadores de categoría 'experto'.
    """
    total = len(jugadores)
    if total == 0:
        return 0.0
    expertos = sum(1 for j in jugadores if j["categoria"] == "experto")
    return (expertos / total) * 100

def estadistica_a4(jugadores: list) -> float | None:
    """
    A4: Promedio de edad de los jugadores de categoría 'avanzado'.
    """
    avanzados = [j["edad"] for j in jugadores if j["categoria"] == "avanzado"]
    if not avanzados:
        return None
    return sum(avanzados) / len(avanzados)

def estadistica_a5(jugadores: list) -> str | None:
    """
    A5: Tipo de saque más usado por los jugadores de categoría 'elite'.
    """
    elites = [j["saque"] for j in jugadores if j["categoria"] == "elite"]
    if not elites:
        return None
    conteo = {saque: elites.count(saque) for saque in TIPOS_SAQUE}
    return max(conteo, key=conteo.get)

# Mostrar resultados
def mostrar_estadisticas(jugadores: list) -> None:
    print("\n" + "=" * 50)
    print("  ESTADÍSTICAS — TEMA A")
    print("=" * 50)

    # A1
    a1 = estadistica_a1(jugadores)
    print(f"\n[A1] Jugadores elite, saque plano, entre 19 y 25 años: {a1}")

    # A2
    a2 = estadistica_a2(jugadores)
    if a2:
        print(f"\n[A2] Jugador de menor edad con más de 50 puntos:")
        print(f"     Nombre   : {a2['nombre']}")
        print(f"     Categoría: {a2['categoria']}")
        print(f"     Edad     : {a2['edad']}")
        print(f"     Puntos   : {a2['puntos']}")
    else:
        print("\n[A2] Ningún jugador tiene más de 50 puntos.")

    # A3
    a3 = estadistica_a3(jugadores)
    print(f"\n[A3] Porcentaje de jugadores 'experto': {a3:.2f}%")

    # A4
    a4 = estadistica_a4(jugadores)
    if a4 is not None:
        print(f"\n[A4] Promedio de edad de jugadores 'avanzado': {a4:.2f} años")
    else:
        print("\n[A4] No hay jugadores de categoría 'avanzado'.")

    # A5
    a5 = estadistica_a5(jugadores)
    if a5:
        print(f"\n[A5] Tipo de saque más usado por jugadores 'elite': {a5}")
    else:
        print("\n[A5] No hay jugadores de categoría 'elite'.")

    print("\n" + "=" * 50)

# Programa principal
def main():
    jugadores = cargar_jugadores()

    if not jugadores:
        print("\nNo se cargaron jugadores. Fin del programa.")
        return

    print(f"\nTotal de jugadores cargados: {len(jugadores)}")
    mostrar_estadisticas(jugadores)

if __name__ == "__main__":
    main()