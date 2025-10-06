#SORTEAR O NOME DE 4 ALUNOS
import random
nome1 = input('fale o nome do aluno: ')
nome2 = input('fale o nome do outro aluno: ')
nome3 = input('fale o nome de mais um aluno: ')
nome4 = input('fale o nome do ultimo aluno: ')
sorteio = random.choice([nome1, nome2, nome3, nome4])
print('o aluno sorteado foi {}'.format(sorteio))