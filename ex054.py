from datetime import date
a = date.today().year
tmaior = 0
tmenor = 0
for p in range(1,8):
    n = int(input('Ano nascimento da {}ª pessoa: '.format(p)))
    i = (a-n)
    if i >= 18:
        tmaior += 1
    else:
        tmenor +=1
print('Total de maiores é {}\nTotal de menores é {}'.format(tmaior,tmenor))
