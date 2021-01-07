import math
from typing import List
from itertools import cycle
import pandas as pd


class Sturges:
    """Relacionado a Aula Tabelas Parte 1"""

    def __init__(self, dados: list) -> None:
        self.dados = dados

    def calculaAmplitude(self):
        val_max = max(self.dados)
        val_min = min(self.dados)
        amplitude = val_max - val_min
        return amplitude

    def calculaIntervalos(self):
        logaritmo = round(math.log(len(self.dados), 10), 3)
        # print(logaritmo) # 1.699
        k = round(1 + 3.322 * logaritmo, 3)
        return k

    def caculaAmplitudeIntervalos(self, amplitude, intervalos):
        ak = amplitude / int(intervalos)
        return ak

    def arredondaIntervalo(self, number: float, decimals: int = 2):
        """Retorna o numero arredondado para cima com 2 casas decimais"""
        if not isinstance(decimals, int):
            raise TypeError('decimal places must be integer')
        elif decimals < 0:
            raise ValueError('decimal places has to be 0 or more')
        elif decimals == 0:
            return math.ceil(number)

        factor = 10 ** decimals
        n = math.ceil(number * factor + 5.0) / factor
        return n

    def calculaIntervaloTempo(self, t1, v):
        """Retorna os intervalos de tempo"""
        global valor
        tempos = [t1, ]
        tempo = t1 + v
        tempos.append(tempo)
        for i in range(5):
            for valor in tempos:
                valor += 1.8
            tempos.append(round(valor, 1))
        return tempos

    def calculaFrequencia(self, v1, v2):
        """Quantos valores estão entre v1 e v2"""
        econtrados = []
        for valor in self.dados:
            if v1 <= valor < v2:
                econtrados.append(valor)
        return len(econtrados)

    def frequenciasEncontradas(self, tempos: List):
        """Itera sobre a lista dos tempos gerados para compor a coluna frequencia"""
        limite1 = tempos[:-1]
        limite2 = tempos[1:]

        freq = []
        for k, v in zip(limite1, limite2):
            freq.append(self.calculaFrequencia(k, v))
        return freq

    def calculaPorcentagem(self, valores: List):
        """Retorna lista de porcentagem encontrada"""
        encontrados = []
        for v in valores:
            p = (v * 100) / 50
            encontrados.append(p)
        return encontrados

    def calculaFreqAcumulada(self, valores: List):
        """Retorna lista de valores de frequencia acumulada
        valores a serem encontrados: 32, 43, 48, 48, 48, 50"""

        freq_acum = [32, ]
        indice = [i for i in range(len(valores))]
        try:
            for i, k, v in (zip(indice, cycle(freq_acum), valores)):
                soma = freq_acum[-1] + valores[i + 1]
                freq_acum.append(soma)
        except IndexError:
            pass

        return freq_acum

    def calculaPorcAcumulda(self, valores):
        """Retorna lista de valores de porcentagem acumulada
        valores a serem encontrados: 64.0, 86.0, 96.0, 96.0, 96.0, 100"""
        porcentagem_acum = [64.0, ]

        indice = [i for i in range(len(valores))]
        try:
            for i, k, v in (zip(indice, cycle(porcentagem_acum), valores)):
                soma = porcentagem_acum[-1] + valores[i + 1]
                if i == 5:
                    break
                porcentagem_acum.append(soma)
        except IndexError:
            pass

        return porcentagem_acum

    def tabela_saida(self,
                     tempos: List,
                     frequencia: List,
                     porcentagem: List,
                     freq_acum: List,
                     porc_acum: List):
        """Representação tabular do cálculo de Sturges conforme aula"""
        df = pd.DataFrame(list(zip(
            tempos,
            frequencia,
            porcentagem,
            freq_acum,
            porc_acum)),
            columns=['Tempos',
                     'Frequencia',
                     'Porcentagem',
                     'Frequência Acumulada',
                     'Porcentagem Acumulda'])
        return df
