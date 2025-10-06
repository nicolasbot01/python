#ler duas notas e fazer a media 
import time
print('Olá aluno, seja bem vindo a sala do futuro aqui você me forneçe a sua nota do primeiro e segundo bimestre e eu mostro a sua media ')
nota1 = int(input('qual é sua primeira nota?'))
nota2 = int(input('qual é sua outra nota?'))
print('carregando...')
time.sleep(2)
media1 = nota1 + nota2
media2 = media1 / 2
print('a media das suas notas deu {}'.format(media2))
