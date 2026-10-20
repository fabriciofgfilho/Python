notas = 0
qnt_notas_info = 0
while True:
    nota = float(input("informe a nota (-1 para finalizar): "))
    if (nota == -1):
        break
    notas = notas + nota
    qnt_notas_info = qnt_notas_info +1

if qnt_notas_info > 0:
    media = notas/qnt_notas_info
    print(f"Quantidade de notas informadas: {qnt_notas_info}")
    print(f"Média: {media:.2f}")

else:
    print("Nenhuma nota informada")

#menu

while True:

    opcao = input("1. Jogar | 2. Configurar | 3. Sair: ")

    if opcao == "1":

        print("Iniciando jogo...")

    elif opcao == "2":

        print("Abrindo configurações...")

    elif opcao == "3":

        print("Saindo... até logo!")

    break # Única forma de encerrar o loop