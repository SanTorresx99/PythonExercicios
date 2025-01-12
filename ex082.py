l = []
p = []
i = []
while True:
    l.append(int(input('Digite um número: ')))
    r = str(input('Continuar? [S/N] '))
    if r in 'Nn':
        break
for i, v in enumerate(l):
    if v%2==0:
        p.append(v)


print(l)
print(p)
print(i)