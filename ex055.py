maior = 0
menor = 0
for p in range(1,6):
    k = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = k
        menor = k
    else:
        if k > maior:
            maior = k
        if k < menor:
            menor = k
print('O maior peso é {}\nO menor peso é {}'.format(maior,menor))



