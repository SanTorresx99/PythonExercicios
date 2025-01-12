#Exercicio 05 Mundo 01 -> programa para: receber um número inteiro e mostrar seu sucessor e seu antecessor

while True:
    try:
        n = int(input('Digite um número: '))
        print('O antecessor de {} é o número {} e seu sucessor é {}'.format(n, (n-1), (n+1)))
        break
    except ValueError:
        print('Entrada inválida. Por favor, digite um número inteiro.')
