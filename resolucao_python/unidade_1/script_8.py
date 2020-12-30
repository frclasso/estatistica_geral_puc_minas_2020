from typing import Dict, List


class CalculaVariabilidade:
    """
Considere as notas das três turmas em uma prova de 10 pontos:
Turma | n | Média | Desvio padrão
    A | 10 | 5 | 1.5
    B | 10 | 5 | 3
    C | 10 | 5 | 4.5
    D | 10 | 3 | 1.5
    E | 10 | 8 | 3
    F | 10 | 5 | 4.5
Calcule o Coeficiente de variacao
----------------------------------
"""
    def __init__(self, dados: List[Dict]) -> None:
        self.dados = dados

    def calcula_variacao(self, turmas):
        """Coeficiente de variação (%)"""
        for data in self.dados:
            for chave, valor in data.items():
                turma = dados[turmas]['turma']
                desvio_padrao = dados[turmas]['desvio']
                media = dados[turmas]['media']
                cv = (desvio_padrao / media) * 100
                return f"Coeficiente de variação da turma {turma} é: {cv}%."


if __name__ == "__main__":
    dados = [
        {'turma': 'A', 'n': 10, 'media': 5, 'desvio': 1.5},
        {'turma': 'B', 'n': 10, 'media': 5, 'desvio': 3},
        {'turma': 'C', 'n': 10, 'media': 5, 'desvio': 4.5},
        {'turma': 'D', 'n': 10, 'media': 3, 'desvio': 1.5},
        {'turma': 'E', 'n': 10, 'media': 8, 'desvio': 3},
        {'turma': 'F', 'n': 10, 'media': 5, 'desvio': 4.5},
    ]
    c = CalculaVariabilidade(dados=dados)
    print(c.__doc__)
    # rodando em toda base de dados
    for num, v in enumerate(dados):
       print(c.calcula_variacao(turmas=num))

