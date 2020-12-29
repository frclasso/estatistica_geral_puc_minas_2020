import math
from typing import List
import statistics


class CaculaTerceiroQuartil:
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

    def calcula_percentil_75(self):
        """Calcula Percentil 75%"""
        percentil = round((75/100) * len(self.dados), 1)
        if isinstance(percentil, float):
            return math.ceil(percentil)  # arredondando pra cima
        else:
            return percentil

    def calcula_primeira_posicao(self, value):
        """Retorna posição a ser avaliada, caso o resultado seja um número inteiro
        fazer a média entre o valor obtido e o valor da próxima posição."""
        posicao = self.dados[value - 1]  # Python inicia a contagem por 0 (zero)
        return posicao

    def calcula_segunda_posicao(self, posicao: int):
        return self.dados[posicao]

    def calcula_terceiro_quartil(self, pos1, pos2):
        """Retorna média entre os valores posicionados na 9a e 10a posição"""
        terceiro_quartil = statistics.mean([pos1, pos2])
        return terceiro_quartil


if __name__ == "__main__":
    tempo_compra = [71, 73, 73, 74, 74, 75, 76, 77, 77, 79, 81, 83]

    c = CaculaTerceiroQuartil(tempo_compra)
    pos = c.calcula_percentil_75()
    valor1 = c.calcula_primeira_posicao(int(pos))
    print(f"Valor da primeira posição encontrada: {valor1}")
    valor2 = c.calcula_segunda_posicao(int(pos))
    print(f"Valor da primeira posição encontrada: {valor2}")
    print(f"Atualmente cerca de 75% dos consumidores estão levando cerca "
          f" de {c.calcula_terceiro_quartil(valor1, valor2)} segundos para efetuar uma compra.")



# TEORIA
"""
    Medidas de posição relativa
    Quartis , Decis e Percentis

    Quartis = (q1, q2, q3)
    Decis = (D1 ... D9)
    Percentis = (p1 ... p99)
"""

"""
    Calculo do percentil
    1) Ordenar dados do menor para o maior;
    2) Calcular posição ocupada pelo percentil (Pk) pela fórmula:
    L = (K/100).n
    onde 'n' é o tamanho da amostra, 'k' é o percentil q se deseja calcular
    e 'L' é a posição do percentil na amostra
"""
