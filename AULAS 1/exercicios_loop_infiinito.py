#exercicio 1

nota = float(input("Digite uma nota entre 0 e 10:" ))

while nota <0 or nota >10:
    print("Nota Inválida !!!" )
    nota = float(input("Digite uma nota entre 0 e 10:" ))

else:
        print("Nota Válida!" )

#exercicio 2

#notas = 0
qnt_notas_info = 0
while True:
    nota = float(input("informe a nota (-1 para finalizar): "))
    if (nota == -1):
        break
    notas = notas + nota
    qnt_notas_info = qnt_notas_info +1

if qnt_notas_info > 0:
    media = notas/qnt_notas_info
    print(f"Quantidade de notas informadas: {qnt_notas_info}, sendo assim temos o total geral das notas em {nota:.2f}.")
    print(f"Sendo assim a média é: {media:.2f}")

else:
    print("Nenhuma nota informada")

#exercicio 3

turmas = int(input("Informe a quantidade de turmas: "))
soma_aluno = 0
contador = 0

while True:
     numeros_aluno = int(input("Informe a quantidade de aluno para cada turma: "))
     if numeros_aluno>40:
        print ("numero maximo de alunos atingido!")
        break
     soma_aluno = soma_aluno + numeros_aluno
     contador = contador + 1
     if contador == turmas:
         break

inf contador > 0:
    media_alunos = soma_aluno/turmas
    print(f"A média de alunos para {turmas} turmas é {media_alunos:.2f}")
     



#exercicio 4

senha = input("Digite uma senha:" )
senha2 = input("Confirme a senha:" )

while senha != senha2:
        print("As senhas não conferem" )

        senha2 = input("Confirme a senha novamente: ")

print("Senha cadastrada com sucesso!")

#exercicio 5
soma = 0

print("Digite números inteiros (digite 0 para encerrar):")

while True:
 
  numero = int(input("Digite um número inteiro: (digite 0 para encerrar)"))

  
  if numero == 0:
    break


  soma = soma + numero

print(f"A soma de todos os números digitados é: {soma}")