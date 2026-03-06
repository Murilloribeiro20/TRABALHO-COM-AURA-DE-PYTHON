Alunos = []

while True:
    quantidade_alunos = int(input("Digite a quantidade de Alunos que serão avaliados: "))

    if quantidade_alunos < 10:
      
      print("Digite Uma quantidade maiores que 10")
      break
 
    for i in range(quantidade_alunos):
 
        nome = input("Digite o nome dos alunos: ")

    notas = []

    for j in range(3):
        nota = float(input("Digite a nota do aluno: "))
        if nota < 0 or nota > 10:
            print("Digite uma nota válida entre 0 e 10.")

            break
        else:
            notas.append(nota)

        





