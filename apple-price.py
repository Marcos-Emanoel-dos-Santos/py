# PREÇO DA MAÇÃ

#1,30 cada se forem menos de 1 dúzia
#1,00 se forem pelo menos 12
programaEstado = 's'
while programaEstado == 's':
    apple = int(input("Quantas maçãs foram compradas? "))
    if apple >= 12:
        print(f"O valor a ser pago é de R${float(apple)*1.0:.2f}")
    else:
        print(f"O valor a ser pago é de R${float(apple)*1.3:.2f}")
    programaEstado = input('Continuar? ')
print("Finalizado")
