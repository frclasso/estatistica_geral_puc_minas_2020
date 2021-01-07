class TabelaCruzada:
    """
----------------------------------------------------------
Tabelas de contingência
Distribuição de frequência do número de defeitos de acordo
com a posiçãp e o lado do pneu em veículos utilitários.
-----------------------------------------------------------
"""

    def caluclaTotais(self, l1, l2):
        """Retorna totais por linha"""
        total = l1 + l2
        return total

    def calculoPercentualLinha(self, l1, l2):
        """Retorna cálculo do percentual por linha"""
        return round(l1 / l2 * 100)


if __name__ == "__main__":
    lado_direito_dianteiro = 32
    lado_direito_traseiro = 28
    lado_esquerdo_dianteiro = 35
    lado_esquerdo_traseiro = 57

    tabela_cruzada = TabelaCruzada()
    print(tabela_cruzada.__doc__)

    print('=' * 26 + ' TABELA 4 ' + '=' * 26)
    pneus_direitos_defeituosos = tabela_cruzada.caluclaTotais(
        lado_direito_dianteiro,
        lado_direito_traseiro)
    print(f'Total de pneus defeituosos LADO DIREITO dianteiro/traseiro:'
          f' {pneus_direitos_defeituosos}')

    pneus_esquerdos_defeituosos = tabela_cruzada.caluclaTotais(
        lado_esquerdo_dianteiro,
        lado_esquerdo_traseiro)
    print(f'Total de pneus defeituosos LADO ESQUERDO dianteiro/traseiro:'
          f' {pneus_esquerdos_defeituosos}')

    total_pneus_dianteiros = tabela_cruzada.caluclaTotais(
        lado_direito_dianteiro,
        lado_esquerdo_dianteiro)
    print(f"Total de pneus dianteiros defeituosos: {total_pneus_dianteiros}")

    total_pneus_traseiros = tabela_cruzada.caluclaTotais(
        lado_direito_traseiro,
        lado_esquerdo_traseiro)
    print(f"Total de pneus traseiros defeituosos: {total_pneus_traseiros}")

    total_geral = tabela_cruzada.caluclaTotais(
        total_pneus_dianteiros,
        total_pneus_traseiros)
    print(f"Total Geral: {total_geral}")

    print('=' * 26 + ' TABELA 5 ' + '=' * 26)

    percentual_linha_1 = tabela_cruzada.calculoPercentualLinha(
        lado_direito_dianteiro,
        pneus_direitos_defeituosos)
    print(f"Percentual Linha - Direito/Dianteira: {percentual_linha_1}%.")

    percentual_linha_2 = tabela_cruzada.calculoPercentualLinha(
        lado_esquerdo_dianteiro,
        pneus_esquerdos_defeituosos)
    print(f"Percentual Coluna - Esquerdo/Dianteira: {percentual_linha_2}%.")

    percentual_linha_3 = tabela_cruzada.calculoPercentualLinha(
        lado_direito_traseiro,
        pneus_direitos_defeituosos)
    print(f"Percentual Linha - Direito/Traseiro: {percentual_linha_3}%.")

    percentual_linha_4 = tabela_cruzada.calculoPercentualLinha(
        lado_esquerdo_traseiro,
        pneus_esquerdos_defeituosos)
    print(f"Percentual Coluna - Esquerdo/Dianteira: {percentual_linha_4}%.")

    percentual_linha_5 = tabela_cruzada.calculoPercentualLinha(
        total_pneus_dianteiros,
        total_geral)
    print(f"Percentual Coluna - Total/Dianteira: {percentual_linha_5}%.")

    percentual_linha_6 = tabela_cruzada.calculoPercentualLinha(
        total_pneus_traseiros,
        total_geral)
    print(f"Percentual Coluna - Total/Traseira: {percentual_linha_6}%.")

    percentual_total_linha_1 = tabela_cruzada.caluclaTotais(
        percentual_linha_1,
        percentual_linha_3
    )
    print(f'Percentual Total Direita - Dianteira: {percentual_linha_1}%'
          f', Traseira: {percentual_linha_3}%, Total: {percentual_total_linha_1}%.')

    percentual_total_linha_2 = tabela_cruzada.caluclaTotais(
        percentual_linha_2,
        percentual_linha_4
    )
    print(f'Percentual Total Esquerda - Dianteira: {percentual_linha_2}%, '
          f'Traseira: {percentual_linha_4}%, Total: {percentual_total_linha_2}%.')

    percentual_total_geral = tabela_cruzada.caluclaTotais(
        percentual_linha_5,
        percentual_linha_6
    )
    print(f'Percentual Total: {percentual_total_geral}%.')

    print('=' * 26 + ' TABELA 6 ' + '=' * 26)

    percentual_coluna_dianteira_direita = tabela_cruzada.calculoPercentualLinha(
        lado_direito_dianteiro,
        total_pneus_dianteiros

    )
    print(f"Percentual por COLUNA - DIANTEIRA/Direita: {percentual_coluna_dianteira_direita}%")

    percentual_coluna_dianteira_esquerda = tabela_cruzada.calculoPercentualLinha(
        lado_esquerdo_dianteiro,
        total_pneus_dianteiros

    )
    print(f"Percentual por COLUNA - DIANTEIRA/Esquerda: {percentual_coluna_dianteira_esquerda}%")

    percentual_coluna_traseira_direita = tabela_cruzada.calculoPercentualLinha(
        lado_direito_traseiro,
        total_pneus_traseiros

    )
    print(f"Percentual por COLUNA - TRASEIRA/direita: {percentual_coluna_traseira_direita}%")

    percentual_coluna_traseira_esquerda = tabela_cruzada.calculoPercentualLinha(
        lado_esquerdo_traseiro,
        total_pneus_traseiros

    )
    print(f"Percentual por COLUNA - TRASEIRA/Esquerda: {percentual_coluna_traseira_esquerda}%")

    percentual_coluna_total_direita = tabela_cruzada.calculoPercentualLinha(
        pneus_direitos_defeituosos,
        total_geral

    )
    print(f"Percentual por COLUNA - TOTAL/Direito : {percentual_coluna_total_direita}%")

    percentual_coluna_total_esquerda = tabela_cruzada.calculoPercentualLinha(
        pneus_esquerdos_defeituosos,
        total_geral

    )
    print(f"Percentual por COLUNA - TOTAL/Esquerdo: {percentual_coluna_total_esquerda}%")

    percentual_total_geral_coluna = tabela_cruzada.caluclaTotais(
        percentual_coluna_total_direita,
        percentual_coluna_total_esquerda
    )
    print(f"Percentual por COLUNA - TOTAL/TOTAL: {percentual_total_geral_coluna}%")

    print('=' * 26 + ' TABELA 7 ' + '=' * 26)

    percentual_coluna_dianteira_direita_tabela_7 = tabela_cruzada.calculoPercentualLinha(
        lado_direito_dianteiro,
        total_geral

    )
    print(f"Percentual por COLUNA - Dianteira/Direito (Tabela 7): "
          f"{percentual_coluna_dianteira_direita_tabela_7}%")

    percentual_coluna_dianteira_esquerda_tabela_7 = tabela_cruzada.calculoPercentualLinha(
        lado_esquerdo_dianteiro,
        total_geral

    )
    print(f"Percentual por COLUNA - Dianteira/Esquerda (Tabela 7): "
          f"{percentual_coluna_dianteira_esquerda_tabela_7}%")

    total_percentual_dianteira = tabela_cruzada.caluclaTotais(
        percentual_coluna_dianteira_direita_tabela_7,
        percentual_coluna_dianteira_esquerda_tabela_7)
    print(f'Total percentual dianteira - tabela 7: {total_percentual_dianteira}%')

    percentual_coluna_traseira_direta_tabela_7 = tabela_cruzada.calculoPercentualLinha(
        lado_direito_traseiro,
        total_geral)
    print(f"Percentual por COLUNA - Traseira/Direito (Tabela 7): "
          f"{percentual_coluna_traseira_direta_tabela_7}%")

    percentual_coluna_traseira_esquerda_tabela_7 = tabela_cruzada.calculoPercentualLinha(
        lado_esquerdo_traseiro,
        total_geral

    )
    print(f"Percentual por COLUNA - Traseira/Direito (Tabela 7): "
          f"{percentual_coluna_traseira_esquerda_tabela_7}%")

    total_percentual_traseira = tabela_cruzada.caluclaTotais(
        percentual_coluna_traseira_direta_tabela_7,
        percentual_coluna_traseira_esquerda_tabela_7)
    print(f'Total percentual traseira - tabela 7: {total_percentual_traseira}%')

    percentual_coluna_total_dianteira = tabela_cruzada.calculoPercentualLinha(
        pneus_direitos_defeituosos,
        total_geral

    )
    print(f"Percentual por COLUNA - TOTAL/Direito : {percentual_coluna_total_dianteira}%")

    percentual_coluna_total_esquerda = tabela_cruzada.calculoPercentualLinha(
        pneus_esquerdos_defeituosos,
        total_geral

    )
    print(f"Percentual por COLUNA - TOTAL/Esquerdo: {percentual_coluna_total_esquerda}%")

    percentualTotal = tabela_cruzada.caluclaTotais(
        percentual_coluna_total_dianteira,
        percentual_coluna_total_esquerda
    )
    print(f"Percentual por COLUNA - TOTAL FINAL: {percentualTotal}%")