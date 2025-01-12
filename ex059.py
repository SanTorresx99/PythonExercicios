n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
op = 0
while op != 5:
    print('''[1] - Somar
[2] - multiplicar
[3] - maior valor
[4] - Escolher novos números
[5] - sair do programa''')
    op = int(input('Qual sua opção? '))
    if op == 1:
        print('a soma de {} + {} é igual a {}'. format(n1,n2,n1+n2))
    elif op == 2:
        print('A multiplicação entre {} x {} é igual a {}'.format(n1,n2,n1*n2))
    elif op == 3:
        if n1>n2:
            print('O maior número digitado foi {}'.format(n1))
        elif n2>n1:
            print('O maior número digitado foi {}'.format(n2))
        else:
            print('Os números são iguais. Você digitou duas vezes o número {}'.format(n1))

    elif op == 4 :
        n1 = int(input('Digite um novo número: '))
        n2 = int(input('Digite um segundo número: '))
    elif op == 5:
        print('finalizando...')
    else:
        print('Escolha uma opção válida (1 ou 2 ou 3 ou 4 ou 5)')
print('Execute para tentar novamente')
