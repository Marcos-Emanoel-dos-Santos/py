from random import randint
from time import sleep
n = randint(0, 5)
print("-=-" * 20)
num = int(input("Diga um número inteiro entre 0 e 5: "))
print("-=-" * 20)
if n == num:
    sleep(2)
    print("Este é o número que o computador pensou, também.")
else:
    sleep(2)
    print(f"O computador pensou um número diferente. Ele pensou {n}")
