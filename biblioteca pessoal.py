
# Dicionário para armazenar os livros e seus status ('disponível' ou 'emprestado')
livros = {}

while True:
    print("\n--- MENU BIBLIOTECA ---")
    print("1. Cadastrar um livro")
    print("2. Pedir livro emprestado")
    print("3. Devolver livro")
    print("4. Consultar lista de livros emprestados")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    #cadastro
    if opcao == "1":
        nome = input("Digite o nome do livro: \n Autor do livro: \n Ano do livro: ")
        if nome in livros:
            print("Erro: Este livro já está cadastrado!")
        else:
            livros[nome] = "disponível"
            print(f"Livro '{nome}' cadastrado com sucesso!")
            
    #pedirlivro
    elif opcao == "2":
        nome = input("Digite o nome do livro que deseja pegar emprestado: ")
        if nome not in livros:
            print("Erro: Este livro não está cadastrado na biblioteca!")
        elif livros[nome] == "emprestado":
            print("Erro: Este livro já está emprestado e não pode ser levado!")
        else:
            livros[nome] = "emprestado"
            print(f"Livro '{nome}' emprestado com sucesso!")
            
    #devolverlivro
    elif opcao == "3":
        nome = input("Digite o nome do livro que deseja devolver: ")
        if nome not in livros:
            print("Erro: Este livro não pertence a esta biblioteca!")
        elif livros[nome] == "disponível":
            print("Aviso: Este livro já consta como disponível na biblioteca.")
        else:
            livros[nome] = "disponível"
            print(f"Livro '{nome}' devolvido com sucesso!")
            
    #consulta
    elif opcao == "4":
        print("\n--- LIVROS EMPRESTADOS ---")
        emprestados = [livro for livro, status in livros.items() if status == "emprestado"]
        
        if not emprestados:
            print("Nenhum livro emprestado no momento.")
        else:
            for livro in emprestados:
                print(f"- {livro}")
                
    #sair
    elif opcao == "5":
        print("Saindo do sistema. Até logo!")
        break
        
    else:
        print("Opção inválida! Por favor, escolha um número entre 1 e 5.")