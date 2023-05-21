#   PRECISEI DE AJUDA

num = int(input("Digite um número entre 1 e 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f" unidades {u}")
print(f"dezenas {d}")
print(f"centenas {c}")
print(f"milhares {d}")
