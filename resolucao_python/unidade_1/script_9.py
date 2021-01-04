import math
import statistics
from typing import List
import matplotlib.pyplot as plt
import numpy as np

# Gráficos Parte 2 - BoxPlot


class BoxCalc:
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
        pos_2 = self.dados[posicao]
        return pos_2

    def calcula_media(self, v1, v2) -> float:
        """Cálculo da média - utlizando o módulo statistics"""
        media = round(statistics.mean([v1, v2]), 4)
        print(f"Valor 1: {v1}")
        print(f"Valor 2: {v2}")
        return media

    def calcula_diq(self, q1, q3):
        diq = q3 - q1
        return diq

    def calcula_limite_discrepante_inferior(self, q1, diq):
        limite_inferior = int(q1 - 1.5 * diq)
        return limite_inferior

    def calcula_limite_discrepante_superior(self, q3, diq):
        limite_superior = int(q3 + 1.5 * diq)
        return limite_superior

    def outlier(self, limite):
        for v in self.dados:
            if v > limite:
                return v


class BoxPlot:

    def __init__(self, q1: int, q2: int, q3: int, dados: List) -> None:
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.dados = sorted(dados)

        data = (18, 21, 27)

        plt.boxplot(data, vert=0)
        plt.title('Graficos Aula 2')
        plt.show()


if __name__ == "__main__":
    dados = [18, 19, 21, 21, 21, 22,
             22, 22, 23, 23, 24, 27]

    calc = BoxCalc(dados)
    q1_pos = calc.calcula_percentil(25)
    print(f"Posição do Primeiro Quartil: {q1_pos}") # 3
    pos1 = calc.calcula_posicao_1(q1_pos)
    pos2 = calc.calcula_posicao_2(q1_pos)
    q1 = calc.calcula_media(pos1, pos2)
    print(f"Q1:{q1}") # 21
    print('-' * 45)

    q2_pos = calc.calcula_percentil(50)
    print(f"Posição do Primeiro Quartil: {q2_pos}")  # 6
    q2_pos1 = calc.calcula_posicao_1(q2_pos)
    q2_pos2 = calc.calcula_posicao_2(q2_pos)
    q2 = calc.calcula_media(q2_pos1, q2_pos2)
    print(f"Q2:{q2}")  # 22
    print('-' * 45)

    q3_pos = calc.calcula_percentil(75)
    print(f"Posição do Primeiro Quartil: {q3_pos}")  # 9
    q3_pos1 = calc.calcula_posicao_1(q3_pos)
    q3_pos2 = calc.calcula_posicao_2(q3_pos)
    q3 = int(calc.calcula_media(q3_pos1, q3_pos2))
    print(f"Q3:{q3}") # 23
    print('-' * 45)

    diq = calc.calcula_diq(q1, q3)
    print(f"Distancia inter-quartílica: {diq}")  # 2

    # Limites de detecção de valores discrepantes
    limite_inferior = calc.calcula_limite_discrepante_inferior(q1, diq)
    print(f"Limite discrepante inferior: {limite_inferior}")  # 18

    limite_superior = calc.calcula_limite_discrepante_superior(q3, diq)
    print(f"Limite discrepante superior: {limite_superior}")  # 26 ####

    outlier = calc.outlier(limite_superior)
    print(f'Valor discrepante(outlier): {outlier}')

    # Gerando o gráfico Box Plot
    boxplot = BoxPlot(q1, q2, q3, dados)
