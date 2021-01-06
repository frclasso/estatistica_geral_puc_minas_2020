from sturges import Sturges


"""
Os dados a seguir representam o tempo(segundos) que operadores gastaram
para montar um equipamento na linha de produção de uma empresa:
4.7, 4.9, 5.1, 5.4, 5.7, 6.0, 6.3, 6.8, 7.3, 8.9,
4.8, 4.9, 5.2, 5.5, 5.7, 6.2, 6.4, 6.9, 8.2, 9.1,
4.8, 5.0, 5.3, 5.6, 5.7, 6.2, 6.5, 7.0, 8.2, 9.9,
4.9, 5.0, 5.4, 5.6, 5.9, 6.2, 6.7, 7.1, 8.3, 14.1,
4.9, 5.0, 5.4, 5.7, 6.0, 6.3, 6.8, 7.3, 8.4, 15.2
"""
tempos = [4.7, 4.9, 5.1, 5.4, 5.7, 6.0, 6.3, 6.8, 7.3, 8.9,
          4.8, 4.9, 5.2, 5.5, 5.7, 6.2, 6.4, 6.9, 8.2, 9.1,
          4.8, 5.0, 5.3, 5.6, 5.7, 6.2, 6.5, 7.0, 8.2, 9.9,
          4.9, 5.0, 5.4, 5.6, 5.9, 6.2, 6.7, 7.1, 8.3, 14.1,
          4.9, 5.0, 5.4, 5.7, 6.0, 6.3, 6.8, 7.3, 8.4, 15.2]

sturges = Sturges(dados=tempos)
amplitude = sturges.calculaAmplitude()
print(f"Amplitude:{amplitude}")

intervalos = sturges.calculaIntervalos()
print(f"Quantidade de intervalos: {intervalos}")

amplitude_intervalos = sturges.caculaAmplitudeIntervalos(amplitude, intervalos)
print(f"Amplitude de intervalos: {amplitude_intervalos}")

variacao = sturges.arredondaIntervalo(amplitude_intervalos)
print(f"Variação: {variacao}")

tempos = sturges.calculaIntervaloTempo(tempos[0], variacao)
print(f'Coluna tempos: {tempos}')

frequencia = sturges.frequenciasEncontradas(tempos)
print(f"Frequências encontradas: {frequencia}")

porcentagem = sturges.calculaPorcentagem(frequencia)
print(f'Porcentagem: {porcentagem}')

frequencia_acumulada = sturges.calculaFreqAcumulada(frequencia)
print(f"Frequência Acumulada: {frequencia_acumulada}")

porcentagem_acumulada = sturges.calculaPorcAcumulda(porcentagem)
print(f"Porcentagem acumulada: {porcentagem_acumulada}")
print()

# representação tabular (pandas)
tabela = sturges.tabela_saida(tempos, frequencia, porcentagem, frequencia_acumulada, porcentagem_acumulada)
print(tabela)