produto = float(input('Digite o preço do produto: R$ '))
desconto = produto * 0.05
preco_final = produto - desconto
print(f"O produto que custava R$ {produto:.2f}, com 5% de desconto, vai custar R$ {preco_final:.2f}.")