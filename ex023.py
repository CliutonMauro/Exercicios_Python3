digitos = int(input('Digite um número: '))

print(f"Analizando o número {digitos}")

unidade = digitos // 1 % 10
dezena = digitos // 10 % 10
centena = digitos // 100 % 10
milhar = digitos // 1000 % 10

print(f"Unidade: {unidade}")
print(f"Dezena: {dezena}")
print(f"Centena: {centena}")
print(f"Milhar: {milhar}")