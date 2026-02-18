

class Carta:
    """Clase de carta de baraja inglesa
    contiene su número y su palo
    """
    def __init__(self, numero: int, palo: str) -> None:
        """Método constructor
        """
        self.numero = numero
        self.palo = palo

    def __str__(self) -> str:
        """Imprime el número de la carta junto a su palo
        
        :return: [El número y el palo de la carta]
        :rtype: [str]
        """
        numero2letra = {11: "J", 12: "Q", 13: "K", 14: "A"}
        return f"{numero2letra.get(self.numero, self.numero)}{self.palo}"
