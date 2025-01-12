n = int(input('Digite um numero inteiro para calcularmos o seu fatorial: '))
c = n
f = 1
print('Calculando {}!'.format(n))
while c > 0:
    print(' {}'.format(c), end='')
    print(' x' if c>1 else ' =', end='')
    f *= c
    c -=1
print('\n {}'.format(f))
#print('O fatorial de {} é igaul a {}'.format(n,f))
