# CONTA QUANTOS NEGATIVOS

num = input("Digite números: ").split()
scan = []
for i in range(len(num)):
    num[i] = int(num[i])
    if num[i] < 0:
        scan.append(num[i])
print(f"Os números negativos são: {scan}")
