

saldo = 1000.00

while True:
    opcao = input("O que deseja realizar? \n1 - Sacar; \n2 - Depositar; \n3 - Sair; ").lower()
    
    if opcao == "sacar":
        valor_saque = float(input("Insira o valor do saque: "))
        if valor_saque <= saldo:
            saldo -= valor_saque 
            print(f"Seu saque foi realizado e seu saldo é R$ {saldo:.2f}")
        else:
            print("Valor de saque maior que o saldo, saque não permitido.")

    elif opcao == "depositar":
        valor_deposito = float(input("Insira o valor do depósito: "))
        saldo += valor_deposito 
        print(f"O saldo após o depósito de R$ {valor_deposito:.2f} é de R$ {saldo:.2f}")

    elif opcao == "sair":
        print("Finalizando o sistema. ")
        break
        
    else:
         
        print("Opção inválida!")
