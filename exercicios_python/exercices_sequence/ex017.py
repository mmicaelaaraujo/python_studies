# cálculo da hipotenusa

# Resolução 1

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = (co ** 2 + ca ** 2) ** (0.5)

print(f'O valor da hipotenusa é {hipotenusa:.2f}')

# Resolução 2

from math import hypot

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = (hypot(co, ca))

print(f'O valor da hipotenusa é {hipotenusa:.2f}')


