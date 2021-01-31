import pandas as pd

"""
Na Tabela 1, temos os dados referentes a alunos matriculados em quatro cursos de
uma universidade em dado ano.
Tabela 1 – Distribuição de alunos segundo o sexo e a escolha do curso.

                    Masculino  Feminino  Total
Curso                                         
Computação                 70        40    110
Matemática                 15        15     30
Estatística                10        20     30
Ciências Aturarias         20        10     30
Total                     115        85    200
"""
data = {
    'Masculino': [70, 15, 10,20, 115],
    'Feminino': [40, 15, 20, 10, 85],
    'Total': [110, 30, 30,30,  200]
}
df = pd.DataFrame(data, index=['Computação', 'Matemática',
                               'Estatística', 'Ciências Aturarias', 'Total'])
df.index.name = 'Curso'
print(df)
print('-' * 60)

"""
    Selecionado-se ao acaso um aluno do conjunto desses quatro cursos 
    determine a probabilidade:
    a) Que o aluno seja do sexo masculino.
    b) Que o aluno esteja matriculado no curso de Estatística.
    c) Que o aluno seja do sexo feminino e matriculado em Matemática.
    d) Que o aluno seja do sexo masculino ou matriculado em Ciências Atuariais.
"""
total_masculino = 115
total_feminino = 85
total_de_alunos = 200
alunos_de_estatistica = 30
matematica_feminino = 15
ciencias_atuarias_masculino = 20

probabilbidade_de_aluno_sexo_masculino =total_masculino/total_de_alunos
print(f"A probabilidade de que o aluno seja do "
      f"sexo masculino: {probabilbidade_de_aluno_sexo_masculino}")

probabilidade_aluno_ser_estatistico = alunos_de_estatistica / total_de_alunos
print(f"A probabilidade de que o aluno esteja matriculado "
      f"no curso de Estatística: {probabilidade_aluno_ser_estatistico}")

probabilidade_ser_aluna_de_matematica =  matematica_feminino / total_de_alunos
print(f"A probabilidade de que Que o aluno seja do sexo feminino "
      f"e matriculado em Matemática: {probabilidade_ser_aluna_de_matematica}")

probabilidade_ser_aluno_ciencias_atuarias = ciencias_atuarias_masculino / total_de_alunos
print(f"A probabilidade de que o aluno seja do sexo masculino ou "
      f"matriculado em Ciências Atuariais: {probabilidade_ser_aluno_ciencias_atuarias}")

p  = (probabilbidade_de_aluno_sexo_masculino) / probabilidade_ser_aluno_ciencias_atuarias
print(p)