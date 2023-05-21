numLista = []
listaPar = []
pares = 0
listaImpar = []
impares = 0
for i in range(10):
    numLista = input("Digite números: ")
    numLista = int(numLista)
    if numLista % 2 == 0:
        print("PAR")
        listaPar.append(numLista)
        pares += 1
    else:
        print("IMPAR")
        listaImpar.append(numLista)
        impares += 1
print("A soma e média dos pares são, respectivamente:")
print(f"{sum(listaPar)} e {sum(listaPar) / pares}")
print("A soma e média dos ímpares são, respectivamente:")
print(f"{sum(listaImpar)} e {sum(listaImpar) / impares}")
