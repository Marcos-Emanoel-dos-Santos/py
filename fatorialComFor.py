estado = 's'
while estado == 's':
    calculo = input("\n Combinatória: 'c' \n Arranjo: 'a' \n Fatorial: 'f' \n")
    num = int(input("Digite um número: "))
    if calculo == 'f':
        f = 1
        if num == 0:
            print("O fatorial é 1")
        elif num < 0:
            print("Não há fatorial de números negativos.")
        else:
            for i in range(1, num + 1):
                f = f * i #FATORIAL = número
            print(f"O fatorial de {num} é {f}")
    if calculo == 'a':
        n = int(input("Quantos termos tem esse arranjo? "))
    estado = input("Continuar calculando? ")
print("Finalizado.")
