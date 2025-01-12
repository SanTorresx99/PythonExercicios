from operator import truediv
from random import randint
cpu = randint (0,10)
print('Oi, vou pensar em um número inteiro entre 0 e 10...\nSerá que você consegue adivinhar?...')
acertou = False
tries = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    tries += 1
    if jogador == cpu:
        acertou = True
    else:
        if jogador < cpu:
            print('Tente um nº maior!')
        else:
            print('Tente um nº menor!')
print('Acertou, miserávi! Escolhi o número {}\nVocê acertou no {}º palpite'.format(cpu,tries))
