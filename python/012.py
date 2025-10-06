#calcular 5% do preço de um produto
import time
print('CUPOM DE DESCONTO DE 5%')  
produto = float(input('qual o valor do produto para eu aplicar o cupom de desconto?'))
desconto = produto * 5 / 100
valor_final = produto - desconto
print('aplicando cupom de desconto...')
time.sleep(1.5)
print('seu produto com desconto ficou {}R$'.format(valor_final))