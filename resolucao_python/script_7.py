import statistics
import math
from typing import List


class MedidasDispersao:
    """
Cálculos das medidas de dispersão: variância e desvio padrõo
------------------------------------------------------------
Considere uma amostra do tempo (em minutos) que funcionários
de uma empresa gastam para chegar ao trabalho:
5, 12, 25, 43, 67
------------------------------------------------------------
"""

    def __init__(self, dados: List) -> None:
        self.dados = dados

    def calcula_media(self) -> float:
        """Cálculando média, usando Python puro """
        media = round(sum(self.dados)/len(self.dados), 4)
        return media

    def calcula_variancia(self, media):
        """Cálculando  variancia, usando Python puro"""
        valores = [(val - media)**2 for val in self.dados]
        variancia = sum(valores)/(len(self.dados)-1)
        return round(variancia, 5)

    def calcula_desvio_padrao(self, variancia):
        """Cálculando desvio padrão, usando Python puro,
        raiz quadrada da variancia"""
        return round(math.sqrt(variancia), 4)


if __name__ == "__main__":
    tempo = sorted([5, 12, 25, 43, 67])
    # print(tempo)
    medidas_disp = MedidasDispersao(tempo)
    media = medidas_disp.calcula_media()
    print(medidas_disp.__doc__)
    print(f"Média: {media}")
    variancia = medidas_disp.calcula_variancia(media)
    print(f"Variancia: {variancia}")
    desvio_1 = medidas_disp.calcula_desvio_padrao(variancia)
    print(f"Os funcionários levam {desvio_1} minutos para chegarem ao trabalho.") # 25.0559