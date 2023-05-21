n = []
for i in range(100):
    n = input("Digite um valor: ")
    if n.isnumeric() == False:
        print("Não é um número!")
    else:
        n = int(n)
        if n % 2 == 0:
            print("PAR")
        else:
             print("IMPAR")
print("Acabaram os espaços!")
