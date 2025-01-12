l = []
q = 0
while True:
    n = int(input('Digite um valor: '))
    r = str(input('Continuar [S/N]')).upper().strip()[0]
    l.append(n)
    if n == 5:
        q += 1
    if r == 'N':
        break
l.sort(reverse=True)
print(f'Você digitou {len(l)} números\nVocê digitou o número 5 {q} vezes\nA lista digitada foi: {l}')