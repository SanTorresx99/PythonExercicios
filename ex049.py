from time import sleep
n = int(input('Escolha um número e veja a sua respectiva tabuada de multiplicar até 10: '))
for c in range (1,11):
    print ('{} x {} = {}'.format(n,c,(n*c)))
