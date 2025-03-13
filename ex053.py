#Confirma se a frase de entrada é um palindromo
f = str(input('Digite a frase: ')).strip().lower()
p = f.split()
j = ''.join(p)
i = ''
for l in range(len(j)-1,-1,-1):
    i += j[l]
print('A frase sem espaços é {} e o inverso {}'.format(j,i))
if j==i:
    print('Temos um palindromo!!!')
else:
    print('Não temos palindromo')
