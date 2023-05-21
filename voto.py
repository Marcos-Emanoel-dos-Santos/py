estado = 's'
while estado == 's':
    ano = int(input("Em que ano você nasceu? "))
    condicao = 2023 - ano
    if condicao < 16:
        print("Você não vota esse ano.")
    else:
        print("Você vota esse ano.")
    estado = input("Continuar? ")
