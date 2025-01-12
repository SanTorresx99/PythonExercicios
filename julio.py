produtos = {
    1: {"nome": "Sanduíche", "preco": 5.00},
    2: {"nome": "Suco", "preco": 2.00},
    3: {"nome": "Refrigerante", "preco": 4.00}
}
print("""Os valores dos produtos são:
1 - Sanduíche - R$ 5,00
2 - Suco - R$ 2,00
3 - Refrigerante - R$ 4,00 """)
while True:
    try:
        p = int(input('Digite o código do Produto: '))
        q = int(input('Digite a quantidade: '))
        break
    except ValueError:
        print("Entrada inválida. Digite números inteiros para o código do produto e a quantidade.")
if p in produtos:
    valor_total = produtos[p]["preco"] * q
    print('Você pediu {} {}. O valor total do pedido será: R$ {:.2f}'.format(q, produtos[p]["nome"], valor_total))
else:
    print("Código do produto inválido.")