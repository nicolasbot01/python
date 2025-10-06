#aumento do salario em 15%
import time
print('AUMENTO DE 15%')
salario = float(input('informe seu salario para eu aplicar o aumento:'))
aumento = salario * 15 / 100
valor_final = salario + aumento
print('infelizmente calculando seu aumento...')
time.sleep(1.7)
print('seu novo sario é {}R$'.format(valor_final))