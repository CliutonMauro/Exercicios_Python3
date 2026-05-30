nome_completo = input("Digite seu nome completo: ")

print("Analisando seu nome...")
print(f"Seu nome em maiúsculas é: {nome_completo.upper()}")
print(f"Seu nome em minúsculas é: {nome_completo.lower()}")

nome_sem_espacos = nome_completo.replace(" ", "")
print(f"Seu nome tem ao todo {len(nome_sem_espacos)} caracteres")

primeiro_nome = nome_completo.split()[0]
print(f"Seu primeiro nome é {primeiro_nome} e tem {len(primeiro_nome)} caracteres")