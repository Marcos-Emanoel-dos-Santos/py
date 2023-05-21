vel = float(input("Digite qual foi a velocidade do carro: "))
if vel <= 80:
    print("Você não terá que pagar multa.")
else:
    print(f"Você pagará uma multa de R${(vel - 80) * 7:.2f}.")
