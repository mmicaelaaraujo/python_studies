# De números reais para inteiros

# Resolução 1:

import math 

from math import trunc

num = float(input('Digite um número: '))

inteiro = math.trunc(num)

print(f'O valor digitado foi {num}, e a sua porção inteira é {inteiro}')
