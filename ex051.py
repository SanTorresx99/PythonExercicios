#Exercício de PA
pt = int(input('Primeiro termo: '))
rz = int(input('Razão da PA: '))
dc = pt + 10 * rz
for c in range(pt,dc,rz):
    print('{}'.format(c),end='->')
