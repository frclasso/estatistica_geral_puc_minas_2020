import math
import statistics
from typing import List

# Gráficos Parte 2 - BoxPlot


class BoxPlot:
    """Considere a seguinte amostra de idade(em anos) de estudantes universitários:
    18, 19, 21, 21, 21, 22,
    22, 22, 23, 23, 24, 27
Vamos construir o boxplot para tais dados e iniciamos calculando as medidas
necessárias
"""
    def __init__(self, dados: List) -> None:
        self.dados = sorted(dados)

    def calcula_percentil(self, quartil):
        """Calcula Percentil"""
        percentil = round((quartil/100) * len(self.dados), 1)
        if isinstance(percentil, float):
            return math.ceil(percentil)  # arredondando pra cima
        else:
            return percentil

    def calcula_posicao_1(self, value):
        """Retorna posição a ser avaliada, caso o resultado seja um número inteiro
        fazer a média entre o valor obtido e o valor da próxima posição."""
        posicao = self.dados[value - 1]  # Python inicia a contagem por 0 (zero)
        return posicao

    def calcula_posicao_2(self, pos):
        """Retorna posição a ser avaliada, caso o resultado seja um número inteiro
        fazer a média entre o valor obtido e o valor da próxima posição."""
        posicao = pos + 1
        pos_2 = self.dados[posicao]  # Python inicia a contagem por 0 (zero)
        return pos_2

    def calcula_media(self, v1, v2) -> float:
        """Cálculo da média - utlizando o módulo statistics"""
        media = round(statistics.mean([v1, v2]), 4)
        print(f"Valor 1: {v1}")
        print(f"Valor 2: {v2}")
        return media

    def calcula_diq(self, q1, q3):
        pass

    def medias_quartis(self):
        pass

    def calcula_limites_discrepantes(self):
        pass


if __name__ == "__main__":
    dados = [18, 19, 21, 21, 21, 22,
             22, 22, 23, 23, 24, 27]

    box = BoxPlot(dados)
    q1_pos = box.calcula_percentil(25)
    print(f"Posição do Primeiro Quartil: {q1_pos}")
    pos1 = box.calcula_posicao_1(q1_pos)
    pos2 = box.calcula_posicao_2(q1_pos)
    q1 = box.calcula_media(pos1, pos2)
    print(f"Q1:{q1}")
    print('-' * 45)

    q2_pos = box.calcula_percentil(50)
    print(f"Posição do Primeiro Quartil: {q2_pos}")
    q2_pos1 = box.calcula_posicao_1(q2_pos)
    q2_pos2 = box.calcula_posicao_2(q2_pos)
    q2 = box.calcula_media(q2_pos1, q2_pos2)
    print(f"Q1:{q2}")
    print('-' * 45)

    q3_pos = box.calcula_percentil(75)
    print(f"Posição do Primeiro Quartil: {q3_pos}")
    q3_pos1 = box.calcula_posicao_1(q3_pos)
    q3_pos2 = box.calcula_posicao_2(q3_pos)
    q3 = int(box.calcula_media(q3_pos1, q3_pos2))
    print(f"Q1:{q3}")
    print('-' * 45)

    diq = q3 - q1
    print(f"Distancia inter-quartílica: {diq}")

    # Limites de detecção de valores discrepantes
    lim1 = int(q1 - 1.5 * diq)
    print(lim1)
    lim2 = int(q3 + 1.5 * diq)
    print(lim2) # 26 #######
