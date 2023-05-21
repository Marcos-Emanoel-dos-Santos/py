num = input("Digite números: ").split()
s = []
for i in range(len(num)):
    num[i] = int(num[i])
    if num[i] < 40:
        s.append(num[i])
print(sum(s))
