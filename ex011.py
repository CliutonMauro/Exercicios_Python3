altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
area_pintada = area / 2

print(f"Sua parede tem a dimensão de {altura} x {largura} e sua área é de {area}m².")
print(f"Para pintar essa parede, você precisará de {area_pintada}l de tinta.")