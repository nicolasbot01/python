#tranformar real em dolar ( considere 1 dolar = 3,27)
import time
real = int(input('quantos reais você tem?'))
dolar = real / 3.27
print('convertendo...')
time.sleep(1.5)
print('você tem {:.2f} dolares'.format(dolar))