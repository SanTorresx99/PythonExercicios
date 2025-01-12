print('Gerador de P.A')
prim = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão da PA? '))
t = prim
c = 1
total = 0
m = 10
while m != 0:
    total = m + total
    while c <= total:
        print('{} -> '.format(t), end='')
        t += r
        c += 1
    print('PAUSA')
    m = int(input('Quantos termos você quer a mais? '))
print('FIM')