#Exercício par/ímpar
while True:
    try:
        n = int(input('Digite um número: '))
        pi = n % 2
        if pi == 0:
            print('O número', n, 'é par.')
        else:
            print('O número', n, 'é ímpar.')
        print('O dobro de', n, 'é', 2 * n)
        print('A raiz de', n, 'é', n ** (1 / 2))
        print('O triplo de', n, 'é', n * 3)
        break
    except ValueError:
        print('Entrada inválida. Por favor, digite um número inteiro.')
