from Jugada import Jugada
from Baraja import Baraja

baraja = Baraja()

while True:
    if len(baraja.cartas) < 5:
        print("Sin cartas suficientes. Fin.")
        break

    opcion_jugador = input("1 = robar | 0 = salir: ")
    if opcion_jugador == "0":
        break
    if opcion_jugador != "1":
        continue

    mano = baraja.coger_n_cartas(5)
    if mano is None:
        print("Sin cartas suficientes. Fin.")
        break

    jugada = Jugada(mano)
    print(jugada)
    print(jugada.datos_jugada())
    print(jugada.nombre_jugada())
