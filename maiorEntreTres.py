print("Você terá que digitar três números.")
n1 = float(input("Digite o primeiro: "))
n2 = float(input("Digite o segundo: "))
n3 = float(input("Digite o terceiro: "))
menor = n1
maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > n3 and n1 > n2:
    maior = n1
if n2 > n3 and n2 > n1:
    maior = n2

print(f"O maior número é {maior} e o menor é {menor}")
