# Preço e Desconto

preco = float(input('Digite o preço do produto: '))

desconto = (preco * 5) / 100

novo_preco = preco - desconto

print(f'O preço do produto com desconto de 5% aplicado é {novo_preco:.2f}!')
