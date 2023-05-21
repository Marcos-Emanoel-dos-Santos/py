num = input("Digite números: ").split()
s = []
for i in range(len(num)):
    num[i] = int(num[i])
    s.append(num[i])
print(f"A soma total é {sum(s)} \n O maior valor é {max(num)}  \n O menor valor é {min(num)}")
