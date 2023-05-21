texto = str(input("Digite um texto: ")).lower().strip()
print(f"A letra 'A' aparece pela primeira vez em {texto.find('a') + 1}")
print(f"A letra A se apresenta {texto.count('a') + 1} vezes")
print(f"A letra A aparece pela última vez em {texto.rfind('a') + 1}")
