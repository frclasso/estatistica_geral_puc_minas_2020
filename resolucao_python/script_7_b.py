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
        """Cálculo da média - utlizando o módulo statistics"""
        media = round(statistics.mean(self.dados), 4)
        return media

    def calcula_variancia(self):
        """Cálculo da variancia - utlizando o módulo statistics"""
        variancia = statistics.variance(self.dados)
        return round(variancia, 5)

    def calcula_desvio_padrao(self):
        """Cálculo do desvio padrão - utlizando o módulo statistics"""
        desvio_padrao = statistics.stdev(self.dados)
        return round(desvio_padrao, 4)


if __name__ == "__main__":
    tempo = sorted([5, 12, 25, 43, 67])
    # print(tempo)
    medidas_disp = MedidasDispersao(tempo)
    media = medidas_disp.calcula_media()
    print(medidas_disp.__doc__)
    print(f"Média: {media}")
    variancia = medidas_disp.calcula_variancia()
    print(f"Variancia: {variancia}")
    desvio_1 = medidas_disp.calcula_desvio_padrao()
    print(f"Os funcionários levam {desvio_1} minutos para chegarem ao trabalho.") # 25.0559