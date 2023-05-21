def maior(lista): #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    maior = 0
    for i in range(len(lista)):
        lista[i] = int(lista[i])
        if lista[i] > maior:
            maior = lista[i]
    return (maior)
def menor(lista): #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menor = lista[0]
    for i in range(len(lista)):
        lista[i] = int(lista[i])
        if lista[i] < menor:
            menor = lista[i]
    return (menor)
def media(lista): #----------------------------------
    media = []
    for i in range(len(lista)):
        lista[i] = int(lista[i])
        media.append(lista[i])
    media = sum(media) / len(lista)
    return media
def fatorial(n): #||||||  |||||  ||||  |||  ||  |
    if n == 0:
        return 1
    else:
        return n*fatorial(n-1)

a = ['1', '2', '5', '8', '12']
print(maior(a))
print(menor(a))
print(media(a))
print(fatorial(5))
