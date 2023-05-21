programaEstado = 1
nota1 = 'incorreta'
nota2 = 'incorreta'
while programaEstado == 1:

    while nota2 == 'incorreta':
        while nota1 == 'incorreta':
            a1 = float(input("Qual foi a nota da primeira avaliação? "))
            if a1 > 10 or a1 < 0:
                print("Verifique o valor digitado.")
                continue
            else:
                nota1 = 'correta'
        a2 = float(input("Qual foi a nota da segunda avaliação? "))
        if a2 > 10 or a2 < 0:
            print("Verifique o valor digitado.")
            continue
        else:
            nota2 = 'correta'
        
    m = (a1 + a2) / 2
    if m >= 6:
        print(f"Média: {m}. APROVADO.")
    else:
        print(f"Média: {m}. REPROVADO.")
    resetar = input("Continuar? ")
    if resetar == "s":
        nota1 = 'incorreta'
        nota2 = 'incorreta'
        continue
    else:
        programaEstado = 0
print("Finalizado.")