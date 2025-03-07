#somando números do loop com critério e contando a qtd de numeros
s = 0
c = 0
for c in range(1,7):
    n = int(input('digite um {}º: '.format(c)))
    if n % 2 == 0:
        s = s + n
        c = c + 1
print ('{} e {}'.format(s,c))
