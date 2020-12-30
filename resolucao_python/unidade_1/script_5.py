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
        media = round(statistics.mean(self.dados), 4)
        return media

    def cacula_desvio_padrao(self, media):
        """Cálculo do desvio padrão"""
        values = [(val - media)**2 for val in self.dados]
        desvio = math.sqrt(sum(values)/(len(self.dados)-1))
        return round(desvio, 5)

    def calc_std_dev(self):
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

    tempo_compra = sorted([71, 73, 73, 74, 74, 75, 76, 77, 77, 79, 81, 83])

    escore = EscoreZ(tempo_compra)
    media = escore.calcula_media()  # 76.08333333333333
    print(f'Media de tempo: {media}')
    print(f"Desvio padrão: {escore.cacula_desvio_padrao(media)}")
    desvio = escore.calc_std_dev()
    print(f"Desvio padrão utilizando o módulo statistics: {desvio}")

    escore_z = round(escore.calcula_escore_z(0, media, desvio), 4)
    print(f"O consumidor está  mais RAPIDO a  {escore_z} desvio padrão  abaixo  da média  do tempo"
          f" gasto entre o início e a finalização da compra.")

    escore_z = round(escore.calcula_escore_z(11, media, desvio), 4)
    print(f"O consumidor está  mais LENTO a  {escore_z} desvio padrão  abaixo  da média  do tempo"
      f" gasto entre o início e a finalização da compra.")