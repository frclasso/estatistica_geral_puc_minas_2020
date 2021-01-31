"""
De acordo com o IBGE(1988) a distribuição  dos suicídios ocorridos no Brasil
em 1986, segundo  a causa atribuída foi a seguinte:

---------------------------------------------------
Causa do suicidio             | Frequência
---------------------------------------------------
Alcoolismo(A)                   263
Dificuldade Financeira(F)       198
Doença mental(M)                700
Outro tipo de doença(O)         189
Desilusão Amorosa(D)            416
Outras causas(C)                217
Total                           1983

Ao selecionarmos aleatoriamente umas das pessoas que tentaram o sucídio,
determine  a probabilidade de que  a causa  atribuída tenha sido:
Desilusão amorosa e Doença Mental
"""


def probabilidadeD():
    desilusao_amorosa = 416
    total = 1983
    p = desilusao_amorosa/total
    return p


pa = probabilidadeD()
print(f'A Probabilidade de o indivíduo ter se suicidado por '
      f'desilusão amorosa P(A) foi:{pa:.4f}')


def probabilidadeM():
    doenca_mental = 700
    total = 1983
    p = doenca_mental/total
    return p


pm = probabilidadeM()
print(f'A Probabilidade de o indivíduo ter se suicidado por '
      f'doença mental P(M) foi:{pm:.4f}')