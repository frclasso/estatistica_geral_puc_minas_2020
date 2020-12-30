import statistics
import math
from typing import List


class DesafioPosRelativa:
    """O Desafio do 0.5 abaixo e 1 acima da média."""

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
        valor = self.dados[posicao]
        escore = (valor - media) / desvio
        return escore

    def calcula_desvio_acima_abaixo(self,
                                    num: float,
                                    media: float,
                                    desvio: float) -> float:
        """Calcula desvios acima ou abaixo da média"""
        valor = (num * desvio) + media
        return round(valor, 4)


if __name__ == "__main__":

    tempo_compra = sorted([71, 73, 73, 74, 74, 75, 76, 77, 77, 79, 81, 83])

    pos_rel = DesafioPosRelativa(tempo_compra)
    media = pos_rel.calcula_media()
    print(f'Media de tempo: {media}')
    desvio = pos_rel.calc_std_dev()
    print(f"Desvio padrão: {desvio}")

    # Qual medida de tempo está a 1 desvio padrão acima da média ? (R: 79,6113)
    print(f"Qual medida de tempo está a 1 desvio padrão acima da "
          f"média? Resposta: {pos_rel.calcula_desvio_acima_abaixo(num=1, media=media, desvio=desvio)}")

    # Qual está a 0.5 desvio padrão abaixo  da média? (R: 74.3193)
    print(f"Qual está a 0.5 desvio padrão abaixo  da média? "
          f"- Resposta: {pos_rel.calcula_desvio_acima_abaixo(num=-0.5, media=media, desvio=desvio)}")