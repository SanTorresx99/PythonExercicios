while True:
    try:
        n = int(input('Digite um número: '))
        print('O antecessor de {} é o número {} e seu sucessor é {}'.format(n, (n-1), (n+1)))
        break
    except ValueError:
        print('Entrada inválida. Por favor, digite um número inteiro.')
