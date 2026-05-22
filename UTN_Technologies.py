
#UTN Technologies - Sistema de Encuesta de Empleados

#  Constantes
TOTAL_ENCUESTAS = 10

GENEROS = {
    "1": "Masculino",
    "2": "Femenino",
    "3": "Otro",
}

TECNOLOGIAS = {
    "1": "IA",
    "2": "RV/RA",
    "3": "IOT",
}

SEPARADOR = "─" * 55
#  Funciones de entrada validada

def pedir_nombre():
    while True:
        nombre = input("Nombre del empleado: ").strip()
        if nombre:
            return nombre
        print("El nombre no puede estar vacío. Intente de nuevo.")


def pedir_edad():
    while True:
        try:
            edad = int(input("  Edad (mínimo 18): ").strip())
            if edad >= 18:
                return edad
            print("La edad debe ser mayor o igual a 18.")
        except ValueError:
            print("Ingrese un número entero válido.")


def pedir_opcion(opciones: dict, etiqueta: str) -> str:
    """Muestra un menú numerado y retorna el valor elegido."""
    for clave, valor in opciones.items():
        print(f"    {clave}. {valor}")
    while True:
        eleccion = input(f"  Seleccione {etiqueta} (número): ").strip()
        if eleccion in opciones:
            return opciones[eleccion]
        print(f"Opción inválida. Ingrese {list(opciones.keys())}.")


# ─────────────────────────────────────────────
#  Carga de encuestas
# ─────────────────────────────────────────────

def cargar_encuestas() -> list[dict]:
    encuestas = []
    print("\n" + SEPARADOR)
    print("UTN TECHNOLOGIES — ENCUESTA DE EMPLEADOS")
    print(SEPARADOR)

    for i in range(1, TOTAL_ENCUESTAS + 1):
        print(f"\n  ── Encuesta {i} de {TOTAL_ENCUESTAS} ──")
        nombre = pedir_nombre()
        edad = pedir_edad()

        print("  Género:")
        genero = pedir_opcion(GENEROS, "género")

        print("  Tecnología preferida:")
        tecnologia = pedir_opcion(TECNOLOGIAS, "tecnología")

        encuestas.append({
            "nombre": nombre,
            "edad": edad,
            "genero": genero,
            "tecnologia": tecnologia,
        })
        print(f"Encuesta guardada para {nombre}.")

    return encuestas
#  Cálculo de métricas
def metrica_1(encuestas: list[dict]) -> int:
    """
    Cantidad de empleados de género Masculino que votaron por IOT o IA,
    cuya edad esté entre 25 y 50 años inclusive.
    """
    cantidad = 0
    for e in encuestas:
        if (
            e["genero"] == "Masculino"
            and e["tecnologia"] in ("IOT", "IA")
            and 25 <= e["edad"] <= 50
        ):
            cantidad += 1
    return cantidad


def metrica_2(encuestas: list[dict]) -> float:
    """
    Porcentaje de empleados que NO votaron por IA,
    siempre y cuando su género no sea Femenino O su edad esté entre 33 y 40.

    Condición de inclusión en el análisis:
        género != Femenino  OR  33 <= edad <= 40

    De ese subconjunto, ¿qué porcentaje no votó por IA?
    """
    subconjunto = [
        e for e in encuestas
        if e["genero"] != "Femenino" or 33 <= e["edad"] <= 40
    ]
    if not subconjunto:
        return 0.0

    no_ia = sum(1 for e in subconjunto if e["tecnologia"] != "IA")
    return (no_ia / len(subconjunto)) * 100


def metrica_3(encuestas: list[dict]) -> list[dict]:
    """
    Nombre y tecnología de los empleados de género Masculino
    con la mayor edad dentro de ese género.
    (Puede haber empate.)
    """
    masculinos = [e for e in encuestas if e["genero"] == "Masculino"]
    if not masculinos:
        return []

    edad_max = max(e["edad"] for e in masculinos)
    return [e for e in masculinos if e["edad"] == edad_max]

#  Presentación de resultados
def mostrar_resultados(encuestas: list[dict]):
    print("\n" + SEPARADOR)
    print("   RESULTADOS DE LA ENCUESTA")
    print(SEPARADOR)

    # ── Métrica 1 ──
    r1 = metrica_1(encuestas)
    print(
        f"\n  1) Masculinos que votaron IOT o IA (entre 25-50 años):\n"
        f"     → {r1} empleado(s)"
    )

    # ── Métrica 2 ──
    r2 = metrica_2(encuestas)
    print(
        f"\n  2) % que no votó por IA\n"
        f"     (género ≠ Femenino  O  edad entre 33-40):\n"
        f"     → {r2:.2f} %"
    )

    # ── Métrica 3 ──
    r3 = metrica_3(encuestas)
    print(
        "\n  3) Masculino(s) de mayor edad:"
    )
    if r3:
        for e in r3:
            print(f"     → {e['nombre']}  |  Tecnología: {e['tecnologia']}  |  Edad: {e['edad']}")
    else:
        print("     → No hay empleados de género Masculino en la encuesta.")

    print("\n" + SEPARADOR + "\n")


#  Punto de entrada
def main():
    encuestas = cargar_encuestas()
    mostrar_resultados(encuestas)

if __name__ == "__main__":
    main()