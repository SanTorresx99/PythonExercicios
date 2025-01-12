from ex115.lib.interface import cabecalho

def arqexiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'Erro ao criar arquivo {nome}')
    else:
        print(f'Arquivo "{nome}" criado com sucesso!')
def lerarq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>4} anos')

    finally:
        a.close()

def cadastroarq(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq,'at')
    except:
        print(f'Erro ao abrir {arq}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao inserir novo cadastro')
        else:
            print(f'Registro adicionado em {arq}')
    finally:
        a.close()


