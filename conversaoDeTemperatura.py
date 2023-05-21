# CONVERTE QUALQUER TEMPERATURA

iniciar = True
while iniciar == True:
    print("Lista de escalas aceitas pelo programa: ")
    print("= Celsius  ===  Fahrenheit  ===  Kelvin =")
    converter = input("Qual escala de temperatura deseja converter? ")
    convertido = input("Para qual escala deseja converter? ")
    if converter == convertido:
        print(f"Este valor já está em {converter} \n")
        continue
    temp = float(input("Digite a temperatura que deseja converter: "))

    if converter == 'Celsius':
        if convertido == 'Fahrenheit':
            temp = temp * 1.8 + 32
            print(f"A temperatura será de {temp}°F \n")
        elif convertido == 'Kelvin':
            temp = temp + 273
            print(f"A temperatura será de {temp}K \n")

    if converter == 'Fahrenheit':
        if convertido == 'Celsius':
            temp = (temp * 5 - 160) / 9
            print(f'A temperatura será de {temp}°C \n')
        elif convertido == 'Kelvin':
            temp = (temp * 5 - 160) / 9 + 273
            print(f'A temperatura será de {temp}K \n')

    if converter == 'Kelvin':
        if convertido == 'Celsius':
            temp = temp - 273
            print(f"A temperatura será de {temp}°C \n")
        elif convertido == 'Fahrenheit':
            temp = 1.8 * (temp - 273) + 32
            print(f"A temperatura será de {temp}°F")
    estado = input("Deseja continuar?")
    if estado == 's':
        iniciar = True
    else:
        iniciar = False
print("Finalizado!")
