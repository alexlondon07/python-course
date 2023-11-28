import random

# Crear una lista de jugadores
jugadores = [
    {"nombre": "Jugador 1", "posicion": "delantero"},
    {"nombre": "Jugador 2", "posicion": "delantero"},
    {"nombre": "Jugador 3", "posicion": "delantero"},
    {"nombre": "Jugador 4", "posicion": "medio campista"},
    {"nombre": "Jugador 5", "posicion": "medio campista"},
    {"nombre": "Jugador 6", "posicion": "medio campista"},
    {"nombre": "Jugador 7", "posicion": "defensa"},
    {"nombre": "Jugador 8", "posicion": "defensa"},
    {"nombre": "Jugador 9", "posicion": "portero"},
    {"nombre": "Jugador 10", "posicion": "portero"},
]


# Función para seleccionar jugadores según la posición
def seleccionar_jugador(jugadores_disponibles):
    jugador = random.choice(jugadores_disponibles)
    jugadores_disponibles.remove(jugador)
    return jugador


# Seleccionar jugadores para el equipo 1
equipo1 = {
    "delantero": seleccionar_jugador([jugador for jugador in jugadores if jugador["posicion"] == "delantero"]),
    "medio campista": seleccionar_jugador(
        [jugador for jugador in jugadores if jugador["posicion"] == "medio campista"]),
    "defensa": seleccionar_jugador([jugador for jugador in jugadores if jugador["posicion"] == "defensa"]),
    "portero": seleccionar_jugador([jugador for jugador in jugadores if jugador["posicion"] == "portero"])
}

# Seleccionar jugadores para el equipo 2
equipo2 = {
    "delantero": seleccionar_jugador([jugador for jugador in jugadores if jugador["posicion"] == "delantero"]),
    "medio campista": seleccionar_jugador(
        [jugador for jugador in jugadores if jugador["posicion"] == "medio campista"]),
    "defensa": seleccionar_jugador([jugador for jugador in jugadores if jugador["posicion"] == "defensa"]),
    "portero": seleccionar_jugador([jugador for jugador in jugadores if jugador["posicion"] == "portero"])
}

# Imprimir los equipos
print("Equipo 1:")
for posicion, jugador in equipo1.items():
    print(f"{posicion}: {jugador['nombre']}")

print("\nEquipo 2:")
for posicion, jugador in equipo2.items():
    print(f"{posicion}: {jugador['nombre']}")
