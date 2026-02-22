from collections import Counter
from Carta import Carta


class Jugada:
    """Clase de jugada de póker que contiene datos sobre la jugada actual

    :param mano: La mano de cartas con la que se está jugando
    :type mano: list[Carta]
    """
    def __init__(self, mano: list[Carta]) -> None:
        """Método constructor
        """
        self.mano = mano

    def datos_jugada(self) -> tuple[int, int]:
        """Método que devuelve dátos sobre la jugada actual

        :return: El código de la jugada y el número de carta a tener en cuenta
        :rtype: tuple[int, int]
        """
        valores = sorted([carta.valor for carta in self.mano])
        palos = [carta.palo for carta in self.mano]
        cantidad_valores = Counter(valores)
        cantidad_palos = Counter(palos)

        es_color = len(cantidad_palos) == 1
        es_escalera = valores == list(range(valores[0], valores[0] + 5))

        if es_escalera and es_color:
            return (8, max(valores))
        if 4 in cantidad_valores.values():
            return (7, max(valor for valor, veces_aparecido in cantidad_valores.items() if veces_aparecido == 4))
        if sorted(cantidad_valores.values()) == [2, 3]:
            return (6, max(valor for valor, veces_aparecido in cantidad_valores.items() if veces_aparecido == 3))
        if es_color:
            return (5, max(valores))
        if es_escalera:
            return (4, max(valores))
        if 3 in cantidad_valores.values():
            return (3, max(valor for valor, veces_aparecido in cantidad_valores.items() if veces_aparecido == 3))
        if list(cantidad_valores.values()).count(2) == 2:
            return (2, max(valor for valor, veces_aparecido in cantidad_valores.items() if veces_aparecido == 2))
        if 2 in cantidad_valores.values():
            return (1, max(valor for valor, veces_aparecido in cantidad_valores.items() if veces_aparecido == 2))
        return (0, max(valores))

    def nombre_jugada(self) -> str:
        """Método que devuelve el nombre de la jugada actual

        :return: Nombre de la jugada actual
        :rtype: str
        """
        t, _ = self.datos_jugada()
        return [
            "Carta alta",
            "Pareja",
            "Doble pareja",
            "Trío",
            "Escalera",
            "Color",
            "Full",
            "Póker",
            "Escalera de color"
        ][t]

    def __str__(self) -> None:
        return " ".join(str(carta) for carta in self.mano)
