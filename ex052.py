n = int(input('Digite um nº: '))
tot = 0
for c in range(1,n+1,1):
    if n % c ==0:
        print('\33[33m', end = ' ')
        tot = tot + 1
    else:
        print('\33[31m',end =' ')
    print('{}'.format(c),end='   ')
print('\n O numero {}, foi divisel {} vezes'.format(n,tot))
if tot == 2:
    print('Por isso ele é um nº primo')
else:
    print('Ele não é primo')