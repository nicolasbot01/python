# ORDEM DE PRECEDENCIA
#1°() primeiro ira resolver os parenteses
#2°** depois a pontencia
#3° *, /, //, % depois multiplicação, divisão, divisão inteira e resto da divisão
#4° +, - e por fim subtração e adição
import time
numero1 = int(input('escreva um numero'))
sucessor = int(numero1 + 1)
antecessor = int(numero1 - 1)
print('analisando sucessor e antecessor...')
time.sleep(1.7)
print('o sucessor do seu numero é {}, e o antecessor é {} e o numero que você escreveu foi {}'.format(sucessor, antecessor, numero1))
