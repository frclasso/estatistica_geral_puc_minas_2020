# Problema 1
"""
    Um pesquisador interessado em avaliar o nível de ruído em um determinado cruzamento
    movimentado da cidade, mediu o nível de ruído (em decibéis) durante 18 dias.
    Os dados encontram-se abaixo:
    85, 92, 95, 98, 99, 101, 103, 105, 107, 110, 112, 114,
    117, 120,120,122, 125, 127
"""
# CALCULO DA MEDIA
dados = [85, 92, 95, 98, 99, 101, 103, 105, 107, 110, 112,
         114, 117, 120, 120, 122, 125, 127]

media = sum(dados)/len(dados)
print(f"A média dos valores é: {media:.2f}")

import statistics
media2 = statistics.median(dados)
print(f"A média dos valores, utilizando statistics, é: {media2}")
print()

# CALCULO DA MEDIANA
# obter os valores nas posições (n/2) e (n + 2/2)
# que sãoo nono e o décimo elemento da lista dados
dados = sorted(dados)
#print(dados)
#print()
posicao_nonoelemento = (len(dados)/2) - 1
# print(posicao_nonoelemento)
nono_elem = dados[int(posicao_nonoelemento)]
#print(nono_elem)
posicao_decimeo_elem = (len(dados)/2)
#print(posicao_decimeo_elem)
decimo_elem = dados[int(posicao_decimeo_elem)]
#print(decimo_elem)

mediana = (nono_elem + decimo_elem) /2
print(f"Mediana: {mediana}")
mediana2 = statistics.mean([nono_elem, decimo_elem])
print(f"Mediana with statistics : {mediana2}")
print()

# CALCULANDO A MODA


def caclula_moda(lista):
    moda = []
    for v in lista:
        repetidos = dados.count(v)
        if repetidos != 1:
            # print(v, repetidos)
            moda.append(v)
    val = set(moda)
    return val


print(f"Moda: {caclula_moda(dados)}")
print(f"Moda usando statistics: {statistics.mode(dados)}")
