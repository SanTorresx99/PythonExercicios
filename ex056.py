soma = 0
q = 0
mih = 0
nhmv = ''
f19 = 0
for p in range(1,5):
    print('-----{}ª pessoa -----'.format(p))
    n = str(input('nome: '))
    i = int(input('idade: '))
    s = str(input('Sexo M/F: ')).strip()
    if s.lower()=='m' and p==1:
        mih=i
        nhmv=n
    if s.lower()=='m' and i > mih:
        mih=i
        nhmv=n
    if s.lower()=='f' and i< 20:
        f19 += 1
    soma += i
    q += 1
m = soma/q
print('a média de idade é {}'.format(m))
print('o nome do homem mais velho é {} e tem {} anos'.format(nhmv,mih))
print('Temos {} mulheres com menos de 20 anos'.format(f19))


