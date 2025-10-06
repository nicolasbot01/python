import time
#fazer um conversor de temperatura de °C para °F
c = float(input('Qual sua temperatura em °C'))
f = c*1.8 
fpt2 = f+32
print('convertendo...')
time.sleep(1.7)
print('sua temperatura convertida em fahrenheit é °F{}'.format(fpt2))