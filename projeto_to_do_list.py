def cadastrar_tarefa():
    
    titulo = input("Informe o título da tarefa: ")
    data = input("Informe a data da tarefa: ")
    
    print("Status da Atividade:")
    print("1 - Feito")  
    print("2 - Não feito")
    op_status = int(input("Escolha o status (1 ou 2): "))
    
    if op_status == 1:
        status = "Feito"
    else:
        status = "Não feito"
        

    tarefa = {
        "titulo": titulo,
        "data": data,
        "status": status
    }
    
    return tarefa


tarefas = [] 
while True:
   
    print("1 - Cadastrar tarefa")
    print("2 - Listar todas")
    print("3 - Sair")
    
   
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("[Erro] Por favor, digite apenas números inteiros!")
        continue
    
    if opcao == 1:
        nova_tarefa = cadastrar_tarefa()
        tarefas.append(nova_tarefa)
        print(">> Tarefa cadastrada com sucesso!")
        
    elif opcao == 2:
        print("LISTA DE TAREFAS")
        
        
        contador = 1
        for t in tarefas:
            print(f"{contador}. Título: {t['titulo']} | Data: {t['data']} | Status: {t['status']}")
            contador += 1 
            

            if opcao == 3:
                print("Saindo...")
            break
    else:
        print("Opção inválida!")