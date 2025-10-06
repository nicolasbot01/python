#60 reais por dia e 15 centavos por km = valor do aluguel
import time
print('PERSCH CARS OS MELHORES EM ALUGUEL DE CARROS')
dia = int(input('Quantos dias o carro foi alugado?:'))
km = int(input('Quantos km você rodou com  carro?:'))
valor1 = dia*60
valor2 = km*0.15
soma = valor1+valor2
print('calculando aluguel...')
time.sleep(1.7)
print('o valor dos dias rodados é R${:.2f} e dos km é R${:.2f} o total a pagar é R${:.2f}'.format(valor1, valor2, soma))