from script_11 import TabelaCruzada
import pandas as pd
from typing import List

"""Representaçãp em tabelas"""

lado_direito_dianteiro = 32
lado_direito_traseiro = 28
lado_esquerdo_dianteiro = 35
lado_esquerdo_traseiro = 57

tabela_cruzada = TabelaCruzada()
print(tabela_cruzada.__doc__)

pneus_direitos_defeituosos = tabela_cruzada.caluclaTotais(
    lado_direito_dianteiro,
    lado_direito_traseiro)

pneus_esquerdos_defeituosos = tabela_cruzada.caluclaTotais(
    lado_esquerdo_dianteiro,
    lado_esquerdo_traseiro)

total_pneus_dianteiros = tabela_cruzada.caluclaTotais(
    lado_direito_dianteiro,
    lado_esquerdo_dianteiro)

total_pneus_traseiros = tabela_cruzada.caluclaTotais(
    lado_direito_traseiro,
    lado_esquerdo_traseiro)

total_geral = tabela_cruzada.caluclaTotais(
    total_pneus_dianteiros,
    total_pneus_traseiros)

percentual_linha_1 = tabela_cruzada.calculoPercentualLinha(
    lado_direito_dianteiro,
    pneus_direitos_defeituosos)

percentual_linha_2 = tabela_cruzada.calculoPercentualLinha(
    lado_esquerdo_dianteiro,
    pneus_esquerdos_defeituosos)

percentual_linha_3 = tabela_cruzada.calculoPercentualLinha(
    lado_direito_traseiro,
    pneus_direitos_defeituosos)

percentual_linha_4 = tabela_cruzada.calculoPercentualLinha(
    lado_esquerdo_traseiro,
    pneus_esquerdos_defeituosos)

percentual_linha_5 = tabela_cruzada.calculoPercentualLinha(
    total_pneus_dianteiros,
    total_geral)

percentual_linha_6 = tabela_cruzada.calculoPercentualLinha(
    total_pneus_traseiros,
    total_geral)

percentual_total_linha_1 = tabela_cruzada.caluclaTotais(
    percentual_linha_1,
    percentual_linha_3
)

percentual_total_linha_2 = tabela_cruzada.caluclaTotais(
    percentual_linha_2,
    percentual_linha_4)

percentual_total_geral = tabela_cruzada.caluclaTotais(
    percentual_linha_5,
    percentual_linha_6)

percentual_coluna_dianteira_direita = tabela_cruzada.calculoPercentualLinha(
    lado_direito_dianteiro,
    total_pneus_dianteiros)

percentual_coluna_dianteira_esquerda = tabela_cruzada.calculoPercentualLinha(
    lado_esquerdo_dianteiro,
    total_pneus_dianteiros)

percentual_coluna_traseira_direita = tabela_cruzada.calculoPercentualLinha(
    lado_direito_traseiro,
    total_pneus_traseiros)

percentual_coluna_traseira_esquerda = tabela_cruzada.calculoPercentualLinha(
    lado_esquerdo_traseiro,
    total_pneus_traseiros)

percentual_coluna_total_direita = tabela_cruzada.calculoPercentualLinha(
    pneus_direitos_defeituosos,
    total_geral)

percentual_coluna_total_esquerda = tabela_cruzada.calculoPercentualLinha(
    pneus_esquerdos_defeituosos,
    total_geral)

percentual_total_geral_coluna = tabela_cruzada.caluclaTotais(
    percentual_coluna_total_direita,
    percentual_coluna_total_esquerda)

percentual_coluna_dianteira_direita_tabela_7 = tabela_cruzada.calculoPercentualLinha(
    lado_direito_dianteiro,
    total_geral)

percentual_coluna_dianteira_esquerda_tabela_7 = tabela_cruzada.calculoPercentualLinha(
    lado_esquerdo_dianteiro,
    total_geral)

total_percentual_dianteira = tabela_cruzada.caluclaTotais(
    percentual_coluna_dianteira_direita_tabela_7,
    percentual_coluna_dianteira_esquerda_tabela_7)

percentual_coluna_traseira_direta_tabela_7 = tabela_cruzada.calculoPercentualLinha(
    lado_direito_traseiro,
    total_geral)

percentual_coluna_traseira_esquerda_tabela_7 = tabela_cruzada.calculoPercentualLinha(
    lado_esquerdo_traseiro,
    total_geral)

total_percentual_traseira = tabela_cruzada.caluclaTotais(
    percentual_coluna_traseira_direta_tabela_7,
    percentual_coluna_traseira_esquerda_tabela_7)

percentual_coluna_total_dianteira = tabela_cruzada.calculoPercentualLinha(
    pneus_direitos_defeituosos,
    total_geral)

percentual_coluna_total_esquerda = tabela_cruzada.calculoPercentualLinha(
    pneus_esquerdos_defeituosos,
    total_geral)

percentualTotal = tabela_cruzada.caluclaTotais(
    percentual_coluna_total_dianteira,
    percentual_coluna_total_esquerda)


def tabela(d1, d2, d3, t1, t2, t3, total1, total2, total3,
           columns: List = None):
    """Representação tabular do cálculo de Sturges conforme aula"""

    dianteira = [d1, d2, d3]
    traseira = [t1, t2, t3]
    total = [total1, total2, total3]
    df = pd.DataFrame(list(zip(
        dianteira,
        traseira,
        total
    )), columns=columns,
        index=['Direito', 'Esquerdo', 'Total'])
    return df


t4 = tabela(
    lado_direito_dianteiro, lado_esquerdo_dianteiro, total_pneus_dianteiros,
    lado_direito_traseiro, lado_esquerdo_traseiro, total_pneus_traseiros,
    pneus_direitos_defeituosos, pneus_esquerdos_defeituosos, total_geral,
    columns=['Dianteira', 'Traseira', 'Total'])

print('=' * 24 + ' TABELA 4 ' + '=' * 24)
print(t4)

t5 = tabela(percentual_linha_1,
            percentual_linha_2,
            percentual_linha_5,
            percentual_linha_3,
            percentual_linha_4,
            percentual_linha_6,
            percentual_total_linha_1,
            percentual_total_linha_2,
            percentual_total_geral,
            columns=['Dianteira(%)', 'Traseira(%)', 'Total(%)'])

print()
print('=' * 24 + ' TABELA 5 ' + '=' * 24)
print(t5)

t6 = tabela(
    percentual_coluna_dianteira_direita,
    percentual_coluna_dianteira_esquerda,
    percentual_total_geral_coluna,
    percentual_coluna_traseira_direita,
    percentual_coluna_traseira_esquerda,
    percentual_total_geral_coluna,
    percentual_coluna_total_direita,
    percentual_coluna_total_esquerda,
    percentual_total_geral_coluna,
    columns=['Dianteira(%)', 'Traseira(%)', 'Total(%)'])

print()
print('=' * 24 + ' TABELA 6 ' + '=' * 24)
print(t6)

t7 = tabela(
    percentual_coluna_dianteira_direita_tabela_7,
    percentual_coluna_dianteira_esquerda_tabela_7,
    total_percentual_dianteira,
    percentual_coluna_traseira_direta_tabela_7,
    percentual_coluna_traseira_esquerda_tabela_7,
    total_percentual_traseira,
    percentual_coluna_total_dianteira,
    percentual_coluna_total_esquerda,
    percentualTotal,
    columns=['Dianteira(%)', 'Traseira(%)', 'Total(%)'])

print()
print('=' * 24 + ' TABELA 7 ' + '=' * 24)
print(t7)
