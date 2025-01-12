p = {'nome':str(input('nome: ')),'nota':int(input('Nota: '))}
if p['nota']>=7:
    print(f'aprovado')
elif p['nota']>=5:
    print(f'recuperação')
else :
    print(f'reprovado')

