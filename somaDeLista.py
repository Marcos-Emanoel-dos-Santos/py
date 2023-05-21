valores = input("Digite os valores ")
val = valores.split()
for i in range(len(val)):
    val[i] = int(val[i])
print(sum(val))
