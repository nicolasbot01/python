#medir altura e largura de uma parede e calcular quantos litros de tinta vai gastar, sabendo que cada litro pinta 2m²
import time 
print('PASSE AS MEDIDAS DE SUA PAREDE PARA REALIZARMOS OS CALCULOS DE LITROS DE TINTAS')
altura = float(input('qual a altura da sua parede?'))
largura = float(input('qual a largura da sua parede'))
m2 = altura * largura
tinta = m2 / 2
print('fazendo as medições e calculando a tinta...')
time.sleep(3)
print('sua parede tem {} m² e você gastara {} litros de tinta'.format(m2, tinta))
