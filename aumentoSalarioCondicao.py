# AUMENTO DE SALÁRIO SE FOR MENOR QUE 1250

salario = float(input("Qual é o salário? "))
if salario <= 1250:
    salario = salario * 1.15
else:
    salario = salario * 1.1
print(f"O salário, depois do aumento, será de R${salario:.2f}")
