n1 = float(input('digite a nota 1: '))
n2 = float(input('digite a nota 2: '))

m = (n1 + n2)/2

if m <= 5:
    print(f'sua nota final é {m}, você reprovou. Estude mais!')
elif m >= 6 and m <= 10:
    print(f'sua nota final é {m}, você está aprovado. Parabéns!')
else:
    print('média inválida!')
