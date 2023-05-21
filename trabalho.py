estado = "s"
while estado == "s":
    horasSemana = float(input("Horas por semana: "))
    valorHora = float(input("Dinheiro por hora: "))
    horasMes = horasSemana * 4
    if horasMes <= 160:
        salario = horasMes * valorHora
    else:
        extra = horasMes - 160
        horasMes = horasMes - extra
        salario = horasMes * valorHora + extra * valorHora * 1.5
    print(f"Seu salário será de R${salario:.2f}")
    estado = input("Continuar? ")
print("Finalizado.")
