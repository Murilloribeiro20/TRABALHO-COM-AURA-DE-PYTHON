alunos = []

while True:
    quantidade_alunos = int(input("Digite a quantidade de Alunos que serão avaliados: "))

    if quantidade_alunos < 10:
      
        print("Digite Uma quantidade maiores que 10")
        break
 
    for i in range(quantidade_alunos):
 
        nome = input("Digite o nome dos alunos: ")
        notas = []

        for n in range(3):
            while True:
                nota = float(input(f"Digite a nota {n + 1}: "))
                if nota < 0 or nota > 10:
                    print("Digite uma nota válida entre 0 e 10.")
                else:
                    notas.append(nota)
                    break

        media = (notas[0] + notas[1] + notas[2]) / 3

        if media >= 7:
            situacao = "Aprovado"
        elif media >= 5:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"

        alunos.append([nome, notas[0], notas[1], notas[2], media, situacao])

    print("Quantidade total de alunos:", len(alunos))

    for aluno in alunos:

        print("\nAluno:", aluno[0])
        print("Notas:", aluno[1], aluno[2], aluno[3])
        print("Média:", round(aluno[4], 2))         #arredondar a media
        print("Situação:", aluno[5])
      
