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

equipo1, equipo2 = crear_equipos(jugadores)

print("Equipo 1:")
for jugador in equipo1:
    print(jugador["nombre"], "-", jugador["posicion"])

print("\nEquipo 2:")
for jugador in equipo2:
    print(jugador["nombre"], "-", jugador["posicion"])


def crear_equipos(jugadores):
    equipo1 = []
    equipo2 = []

    jugadores_por_posicion = {}

    for jugador in jugadores:
        posicion = jugador["posicion"]
        if posicion not in jugadores_por_posicion:
            jugadores_por_posicion[posicion] = []
        jugadores_por_posicion[posicion].append(jugador)

    for posicion, lista_jugadores in jugadores_por_posicion.items():
        for i, jugador in enumerate(lista_jugadores):
            if i % 2 == 0:
                equipo1.append(jugador)
            else:
                equipo2.append(jugador)

    return equipo1, equipo2