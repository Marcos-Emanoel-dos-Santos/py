#   PRECISEI DE AJUDA

nome = input("Digite o nome: ")
print(f"Nome em maiúsculas: {nome.upper()}")
print(f"Nome em minúsculas: {nome.lower()}")
print(f"Este nome tem {len(nome) - nome.count(' ')} letras")
nome = nome.split()
print(f"O primeiro nome tem {len(nome[0])} letras")
