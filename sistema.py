from time import sleep
from ex115.lib.arquivo import *
from ex115.lib.interface import *
arq = 'cursoemvideo.txt'
if not arqexiste(arq):
    criararq(arq)
else:
    print(f'Arquivo {arq} encontrado')
while True:
    resp = menu(['VER CADASTROS','CADASTRAR PESSOAS','SAIR DO SISTEMA'])
    if resp == 1:
        #Opção de listar conteúdo do arquivo
        lerarq(arq)
        sleep(1)
    elif resp == 2:
        #Cadastrar pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastroarq(arq, nome, idade)
        sleep(10)
    elif resp == 3:
        print('Opcao 3 foi escolhida\nSaindo do sistema ... Até logo')
        break
    else:
        print('...')
        sleep(1)
        print('\033[31mOPÇÃO INVALIDA!\nTENTE NOVAMENTE COM UMA OPÇÃO VÁLIDA\033[m')