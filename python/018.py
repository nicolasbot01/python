import math
ângulo = float(input('digite o angulo:'))
seno = math.sin(math.radians(ângulo))
coseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print('em um ângulo de {}° o seno é {:.2f}, o coseno é {:.2f} e a tangente é {:.2f}'.format(ângulo, seno, coseno, tangente))