# SE O PRIMEIRO NÚMERO É MAIOR QUE O SEGUNDO, SEU VALOR DOBRA
# CASO CONTRÁRIO, O VALOR DO SEGUNDO É DIVIDIDO POR 2

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
if n1 > n2:
    print(n1 * 2)
else:
    print(n2 / 2)
