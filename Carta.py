

class Carta:
    """Clase de carta de baraja inglesa, contiene su símbolo y su palo
    """
    def __init__(self, valor: int, palo: str) -> None:
        """Método constructor
        """
        self.valor = valor
        self.palo = palo

    def __str__(self) -> str:
        """Imprime el símbolo de la carta junto a su palo
        
        :return: El símbolo y el palo de la carta
        :rtype: str
        """
        valor2letra = {11: "J", 12: "Q", 13: "K", 14: "A"}
        return f"{valor2letra.get(self.valor, self.valor)}{self.palo}"
