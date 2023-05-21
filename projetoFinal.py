# DIGITAR QUANTOS ALUNOS. MEDIA E NOME DE CADA UM. ESCREVER EM ORDEM ALFABETICA.
iniciar = True
while iniciar == True:
    alunos = int(input("Numero de alunos: "))
    alunos_lista = []
    AVs = int(input("Quantidade de avaliações: "))

    for aluno in range(alunos):
        notas_lista = []
        nome = input("Digite o nome completo do aluno: ")
        for nota in range(AVs):
            nota = int(input(f"Digite a {nota + 1}° nota do aluno: "))
            notas_lista.append(nota)
        print(f"A média de {nome} é {sum(notas_lista) / AVs:.1f}")
    for aluno in range(alunos):
        alunos_lista.append(aluno)
        for i in alunos_lista:
            print(f"A média de {alunos_lista[i]} é de {nota}")

    resetar = input("Colocar uma nova lista? (s/n) ")
    if resetar == 's':
        iniciar = True
    else:
        iniciar = False
