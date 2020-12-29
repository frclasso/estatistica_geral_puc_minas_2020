from typing import List
import statistics
import math


class CaculaQuartoQuartil:
    """
    PROBLEMA 2
        Um pesquisador está interessado em avaliar o tempos (em segundos) que os
        consumidores demoram entre o início e a finalização de uma compra em um
        determinado site na internet. Para isso, observou 12 consumidores escolhidos
        aleatoriamente no sistema. Os dados encontram-se abaixo:
        71, 73, 73, 74, 74, 75
        76, 77, 77, 79, 81, 83
    """

    def __init__(self, dados: List) -> None:
        self.dados = dados

    def calcula_percentil(self) -> int:
        """Quarto quartil corresponde ao quarto decil, 40/100
        Valor decimal deve ser arredondado para cima."""
        percentil = round((40/100) * len(self.dados), 1)
        if isinstance(percentil, float):
            return math.ceil(percentil)  # arredondando pra cima (4.8)
        else:
            return percentil

    def calcula_posicao(self, value):
        """Retorna posição a ser avaliada, caso o resultado seja um número inteiro
        fazer a média entre o valor obtido e o valor da próxima posição."""
        posicao = self.dados[value - 1]  # Python inicia a contagem por 0 (zero)
        return posicao


if __name__ == "__main__":

    tempo_compra = [71, 73, 73, 74, 74, 75, 76, 77, 77, 79, 81, 83]

    c = CaculaQuartoQuartil(tempo_compra)
    perc = c.calcula_percentil()
    print(f"Percentil [Posição] {perc}")
    print(f"Valor correspondente a Posição: {c.calcula_posicao(perc)}")
    print(f"Atualmente 40% dos demoram até {c.calcula_posicao(perc)} segundos"
          f" entre o início e a finalização da compra")


