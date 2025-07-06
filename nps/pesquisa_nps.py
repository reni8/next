"""Esse módulo executa uma pesquisa de satisfação de clientes utilizando os métodos da classe Nps"""

from nps import Nps

print('*** Pesquisa de Satisfação ***')

pesquisa = Nps()

while True:
    nota = input('Em uma escala de 0 a 10, o quanto você recomendaria nossa empresa?'
    '\nDigite "fim" para encerrar a pesquisa: ')

    if nota == "fim":
        break
    pesquisa.adicionar_nota(int(nota))

print(f'Valor do NPS = {pesquisa.calcular_nps()}')
pesquisa.avaliar_classificacao()
