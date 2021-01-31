import pandas as pd

"""
Suponha que você é o gerente de uma fábrica de sorvetes. 
Você sabe que 20% de todo o leite que utiliza na fabricação dos sorvetes 
provém da fazenda F1, 30% são de uma outra fazenda F2 e 50% de uma fazenda F3. 
Um órgão de fiscalização inspecionou as fazendas de surpresa, e observou que
20% do leite produzido por F1 estava adulterado por adição de água, enquanto que 
para F2 e F3, essa proporção era de 5% e 2%, respectivamente. 
Na indústria de sorvetes que você gerencia os galões de leite são armazenados
em um refrigerador sem identificação das fazendas. Para um galão escolhido ao acaso, 
calcule:
a) A probabilidade de que o galão contenha leite adulterado.
b) A probabilidade de que o galão tenha vindo da fazenda F3, sabendo que
 contém leite não adulterado.

"""
p_f_1_a = 0.2
p_f_2_a = 0.05
p_f_3_a = 0.02
p_f1 = 0.2
p_f2 = 0.3
p_f3 = 0.5
p_f3_a_c = 1 - p_f_3_a

# a) A probabilidade de que o galão contenha leite adulterado.
probabilidade_leite_adulterado = (p_f_1_a * p_f1) + (p_f_2_a * p_f2) + (p_f_3_a * p_f3)
print(f"A probabilidade de que o galão contenha "
      f"leite adulterado é de: {probabilidade_leite_adulterado}")

# b) A probabilidade de que o galão tenha vindo da fazenda F3, sabendo que
#  contém leite não adulterado.

leite_f3 = p_f3_a_c * p_f3 / 1 - probabilidade_leite_adulterado
print(f"A probabilidade de que o galão tenha vindo da fazenda F3, "
      f"sabendo que contém leite não adulterado.{leite_f3}")