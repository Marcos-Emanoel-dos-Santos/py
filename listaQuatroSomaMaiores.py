lista = input("Lista de 4 números: ")
numLista = lista.split()
for n in range(len(numLista)):
    numLista[n] = int(numLista[n])
numLista.sort()
print(numLista[n] + numLista[n - 1])
