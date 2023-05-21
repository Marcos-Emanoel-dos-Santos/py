# EQUAÇÃO DE SEGUNDO GRAU

from math import sqrt
print("\033[33m#-#\033[m" * 20)
print("\033[34mAlgoritmo de resolver equações de segundo grau.\033[m")
print("\033[33m#-#\033[m" * 20)
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
print(f"A equação é {a}x² + {b}x + {c} = 0")
delta = b*b - 4 * a * c
if delta < 0:
    print("Sua equação não tem soluções reais.")
elif delta == 0:
    print("Sua equação tem duas soluções iguais, seu resultado é:")
    print(f"\033[31m{(b*b - delta) / 2 * a}\033[m")
else:
    print("Sua equação possui dois valores reais, são eles: ")
    print(f"\033[31m{(b*b - sqrt(delta)) - 2 * a:.2f}\033[m")
    print(f"\033[31m{(b*b + sqrt(delta)) - 2 * a:.2f}\033[m")
