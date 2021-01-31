import pandas as pd
import math

data = {
    'Homicidio(H)': [12, 39, 18, 69],
    'Furto(F)': [379, 106, 20, 505],
    'Assalto(A)': [727, 642, 57, 1426],
    'Total': [1118, 787, 95, 2000]
}

df = pd.DataFrame(data, index=['Estranho(E)', 'Conhecido(C)', 'Ignorado(I)', 'Total'])
df.index.name = 'Criminoso'
print(df)
print()

"""
Se uma pessoa é escolhida ao acaso entre os estudados na amostra. 
Determine as probabilidades de:
    a.) Ter sofrido um homicídio ou ter sido vítima de um estranho.
    b.) Dado que a pessoa sofreu um assalto, ter sido vítima de um conhecido. 
    c.) A pessoa ter sofrido um furto, dado que ela foi vítima de um estranho.
"""

total_de_homicidios = 2000

total_homicidio = 69
total_estranho = 1118

homicidios = {12, 39, 18, 69}
estranhos = {12, 379, 727, 1118}


def vitima_hommicidio():
    return total_homicidio / total_de_homicidios


def vitima_de_estranho():
    return total_estranho / total_de_homicidios


vitimas_hom_estranho = homicidios.intersection(estranhos)

vitima_h_e = list(homicidios.intersection(estranhos))[0] / total_de_homicidios

print(f'Vítima de Homicídio P(H): {vitima_hommicidio()}')
print(f'Vítima de Estranho P(E): {vitima_de_estranho()}')
print(f"Ter sofrido um homicídio ou ter sido vítima de um estranho: {vitima_h_e:.3f}")

# b.) Dado que a pessoa sofreu um assalto, ter sido vítima de um conhecido.
conhecido = 642
total_assaltos = 1426

probabilidade_de_assalto_por_conhecido = conhecido / total_de_homicidios
probabilidade_assalto = total_assaltos / total_de_homicidios
vitima_de_um_conhecido = probabilidade_de_assalto_por_conhecido/ probabilidade_assalto
print(f"Dado que a pessoa sofreu um assalto, "
      f"ter sido vítima de um conhecido: {vitima_de_um_conhecido:.3f}")

# c.) A pessoa ter sofrido um furto, dado que ela foi vítima de um estranho.
furto = 379
furto_e_vitima_de_estranho = furto / total_estranho
print(f"A pessoa ter sofrido um furto, dado que ela foi "
      f"vítima de um estranho: {furto_e_vitima_de_estranho:.3f}")
