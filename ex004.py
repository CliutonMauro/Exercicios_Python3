palavra = input('Digite algo: ')
print(f"O tipo primitivo desse valor é {type(palavra)}.")
print(f"Só tem espaços? {palavra.isspace()}") # Verifica se a string é composta apenas por espaços em branco.
print(f"É um número? {palavra.isnumeric()}") # Verifica se a string é composta apenas por caracteres numéricos.
print(f"É alfabético? {palavra.isalpha()}") # Verifica se a string é composta apenas por caracteres alfabéticos.
print(f"É alfanumérico? {palavra.isalnum()}") # Verifica se a string é composta por caracteres alfanuméricos.
print(f"Está em maiúsculas? {palavra.isupper()}") # Verifica se todos os caracteres da string estão em maiúsculas.
print(f"Está em minúsculas? {palavra.islower()}") # Verifica se todos os caracteres da string estão em minúsculas.
print(f"Está capitalizada? {palavra.istitle()}") # Verifica se a string está no formato de título (primeira letra de cada palavra em maiúscula).