# Aluguel de carro

km = float(input('Digite a quantidade de km rodados: '))
dias = int(input('Digite a quantidade total de dias de aluguel do carro: '))

calculo_km = km * 0.15
calculo_dias = dias * 60

valor_total = calculo_km + calculo_dias

print(f' O valor total a ser pago é {valor_total:.2f}!')