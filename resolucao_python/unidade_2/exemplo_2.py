import pandas as pd

"""Estudo de relação entre o hábito de fumar e a causa  da morte, 
entre 1000 empresários"""

data = {
        'Câncer(C)': [135, 55, 190],
        'Doença Cardíaca(D)': [310, 155, 465],
        'Outros(O)': [205, 140, 345],
        'Total': [650, 350, 1000]
    }

df = pd.DataFrame(data, index=['SIM','NAO', 'TOTAL'])
df.index.name = 'Fumante'

print(df)

"""
         Câncer(C)  Doença Cardíaca(D)  Outros(O)  Total
Fumante                                                 
SIM            135                 310        205    650
NAO             55                 155        140    350
TOTAL          190                 465        345   10000

"""

"""
    Um indivíduo é selecionado aleatoriamente entre os observados na amostra. 
    Determine as seguintes probabilidades:
    a.) Ser fumante.
    b.) Ter morrido de câncer.
    c.) Não ser fumante e ter morrido de doença cardíaca. 
    d.) Ser fumante ou ter morrido de outras causas
"""
print()
total_obitos = 1000


def fumantes():
    total_fumantes = 650
    return total_fumantes/total_obitos


def cancer():
    cancer = 190
    return cancer/total_obitos


def cardiacoNaoFumante():
    cardiaco_nao_fum = 155
    return cardiaco_nao_fum/total_obitos


def fumanteOutros():
    fum = fumantes()
    outros_total = 345 / total_obitos
    outros = 205 / total_obitos
    return fum + outros_total - outros


fumantes_obitos = fumantes()
print(f'Total de óbitos entre os fumantes: {fumantes_obitos}')

obitos_por_cacer = cancer()
print(f'Total de óbitos entre por câncer: {obitos_por_cacer}')

cardiaco_nao_fumante = cardiacoNaoFumante()
print(f'Total de óbitos entre os Cardíacos Não Fumantes: {cardiaco_nao_fumante}')

f = fumanteOutros()
print(f'Total de fumantes que morreram de outras causas: {f:.3f}')