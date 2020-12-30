import statistics
import math
from typing import List


class Desafio:
    """10% dos consumidores mais rápidos demoram no máximo,
    quantos segundos entre o início e a finalização da compra?"""

    def __init__(self, dados: List) -> None:
        self.dados = dados

    def calcula_percentil(self, percentual) -> int:
        """Calculo do percentil percentil/100
        Valor decimal deve ser arredondado para cima."""
        percentil = round((percentual/100) * len(self.dados), 1)
        # print(percentil)
        if isinstance(percentil, float):
            return math.ceil(percentil)  # arredondando pra cima
        else:
            return percentil

    def calcula_posicao(self, value):
        """Retorna posição a ser avaliada, caso o resultado seja um número inteiro
        fazer a média entre o valor obtido e o valor da próxima posição."""
        posicao = self.dados[value - 1]  # Python inicia a contagem por 0 (zero)
        # print(posicao)
        return posicao


if __name__ == "__main__":

    tempo_compra = [71, 73, 73, 74, 74, 75, 76, 77, 77, 79, 81, 83]

    calculo = Desafio(tempo_compra)

    percentil_10 = calculo.calcula_percentil(10)
    # print(f'Percentil arredondado: {percentil_10}')
    print()
    print(f"Os 10% mais rápidos gastaram: {calculo.calcula_posicao(percentil_10)} segundos.")
    print('-'* 42)

    """20% é o universo mais lento, logo 80% são os mais råpidos"""
    percentil_20 = calculo.calcula_percentil(80)
    print(f"Os 20% mais lentos gastaram: {calculo.calcula_posicao(percentil_20)} segundos.")