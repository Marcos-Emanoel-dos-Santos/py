fixo = float(input("Digite o salário do funcionário. "))
tot = float(input("Digite qual foi o total de vendas do funcionário. "))
if tot <= 1500:
    salario = fixo + tot * 3/100
else:
    extra = tot - 1500
    extra = extra * 5/100
    sem_extra = 1500 * 3/100
    salario = fixo + sem_extra + extra
print(f"O salário deste funcionário é de R${salario:.2f}")
