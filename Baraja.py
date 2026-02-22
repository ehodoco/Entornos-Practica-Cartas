import random
from Carta import Carta


class Baraja:
    """Clase de baraja que contiene una baraja de cartas inglesa
    """
    def __init__(self):
        """Método constructor
        Crea una carta con cada valor y tipo y las mezcla
        """
        self.cartas = [Carta(valor, palo) for valor in range(2, 15) for palo in ["♠", "♥", "♦", "♣"]]
        random.shuffle(self.cartas)


    def coger_carta(self) -> Carta:
        """Método que devuelve la última carta de la baraja

        :return: La última carta de la baraja si quedan cartas en la baraja, `None` si no queda ninguna
        :rtype: object
        """
        if not self.cartas:
            return None
        return self.cartas.pop()


    def coger_n_cartas(self, n: int) -> list[Carta]:
        """Método que devuelve n número de cartas de la baraja

        :param n: El número de cartas que se van a escoger
        :type n: int

        :return: Una lista que contiene n número de cartas si hay más de n cartas en la braja, `None` si no hay más de n cartas en la baraja
        :rtype: list[Carta]
        """
        if len(self.cartas) < n:
            return None
        return [self.coger_carta() for _ in range(n)]


