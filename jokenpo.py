from random import choice
jogoEstado = "sim"
while jogoEstado == "sim" or jogoEstado == "s":
    print("Pedra, papel, tesoura...")
    escolha = input("... ")
    escolhaBot = choice(['pedra', 'papel', 'tesoura'])
    print(escolhaBot)
    if escolha == escolhaBot:
        print("Empate!")
    elif escolha == 'tesoura' and escolhaBot == 'pedra':
        print("Bot: Ganhei!")
    elif escolha == 'pedra' and escolhaBot == 'papel':
        print("Bot: Ganhei!")
    elif escolha == 'papel' and escolhaBot == 'tesoura':
        print("Bot: Ganhei!")
    else: print("Bot: Perdi!")
    jogoEstado = input("Jogar denovo? ")
print("Entendi :(")
