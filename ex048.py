#Contar de 2 em 2 até 500, contando numeros diviseis por 3
c = 0
s = 0
for c in range(1,501,2):
    if c % 3 ==0:
        s += c
        c += 1
print('{}   {}'.format(s,c))
