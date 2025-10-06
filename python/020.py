import random, time
nome1 = input('fale o nome de um aluno: ')
nome2 = input('fale o nome de um aluno: ')
nome3 = input('fale o nome de um aluno: ')
nome4 = input('fale o nome de um aluno: ')
print('escolhendo...')
time.sleep(1.7)
print(random.sample([nome1, nome2, nome3, nome4], 4))