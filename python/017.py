import math
cateto_adjacente = float(input('qual o cateto adjacente? '))
cateto_oposto = float(input('qual o cateto oposto'))
hipotenusa =  math.sqrt((cateto_adjacente**2)+(cateto_oposto**2))
print('o valor da hipotenusa é {:.2f}'.format(hipotenusa))