#ler valor em metros e transformar em centimetros e milimetros
# km hm dam m dm cm mm
import time
print('me informe um valor em metros que transformarei em centimetros e milimetros ')
metros = float(input('quantos metros?'))
cm = metros * 100
mm = metros * 1000
km = metros / 1000
hm = metros / 100
dm = metros * 10
dam = metros / 10
print('transformando...')
time.sleep(3)
print('\n sua medida em quilometros é {}km \n sua medida em hectometro é {}hm \n sua medida em decametro é {}dam \n sua medida em decimetros é {}dm \n sua mediada em centimetros é {}cm \n e sua medida em milimetros é {}mm'.format(km, hm, dam, dm, cm, mm))