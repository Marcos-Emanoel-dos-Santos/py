a = float(input("Digite o comprimento do primeiro lado: "))
b = float(input("Digite o comprimento do segundo lado: "))
c = float(input("Digite o comprimento do terceiro lado: "))
if a < b + c and b < a + b and c < a + b:
    print("Os três segmentos dados podem formar um triângulo.")
else:
    print("Os três segmentos dados não podem formar um triângulo.")
