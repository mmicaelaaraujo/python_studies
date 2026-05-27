# Cálculo Área

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura * altura

qnt_tinta = area / 2

print(f' Para pintar uma área de {area}m^2, serão necessários {qnt_tinta} litros de tinta!')
