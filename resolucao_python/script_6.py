import statistics
import math
from typing import List


class EscoreZ:
    """O objetivo de se calcular o escore Z é expressar em unidades de
    desvio padrão quanto um determinado número está distante da média
    Para o cálculo do escore Z é necessário conhecer a média eo desvio padrão"""

    def __init__(self, dados: List) -> None:
        self.dados = dados

    def calcula_media(self) -> float:
        med = round(statistics.mean(self.dados), 4)
        return med

    def calc_std_dev(self) -> float:
        """Utilizando o modulo statistics para calculcar desvio padrão"""
        return round(statistics.stdev(self.dados), 5)

    def calcula_escore_z(self, posicao: int, media: float, desvio: float) -> float:
        """Mede a distância de cada valor da amostra em relação a média
        Formula:
        Escore Z = valor - media / desvio padrao
        """
        menor_valor = self.dados[posicao]
        escore = (menor_valor - media) / desvio
        return escore


if __name__ == "__main__":

    tempo_compra = [71, 73, 73, 74, 74, 75, 76, 77, 77, 79, 81, 83]

    escore = EscoreZ(tempo_compra)
    media = escore.calcula_media()
    print(f'Media de tempo: {media}')
    desvio = escore.calc_std_dev()
    print(f"Desvio padrão: {desvio}")

    # escore_z = round(escore.calcula_escore_z(9, media, desvio), 4)
    # print(f"O consumidor está  mais RAPIDO a  {escore_z} desvio padrão  abaixo  da média  do tempo"
    #       f"gasto entre o início e a finalização da compra.")

    # Qual medida de tempo está a 1 desvio padrão acima da média ? (R: 79,6113)

    # Qual está a 0.5 desvio padrão abaixo  da média? (R: 74.3193)
