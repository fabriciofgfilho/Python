

Python
def cadastrar_tarefa():
    """Função para cadastrar uma nova tarefa e retornar um dicionário com os dados."""
    print("\n--- Cadastro de Nova Tarefa ---")
    
    titulo = input("Informe o título da tarefa: ")
    data = input("Informe a data da tarefa (ex: 15/08/2026): ")
    
    # Validação simples de status
    print("\nStatus da Atividade:")
    print("1 - Feito")
    print("2 - Não feito")
    op_status = int(input("Escolha o status (1 ou 2): "))
    
    if op_status == 1:
        status = "Feito"
    else:
        status = "Não feito"
        
    # Criando o dicionário da tarefa conforme solicitado na Aula 06
    tarefa = {
        "titulo": titulo,
        "data": data,
        "status": status
    }
    
    print(f">> Tarefa '{titulo}' cadastrada com sucesso!")
    return tarefa


def listar_tarefas(lista_de_tarefas):
    """Função para listar todas as tarefas cadastradas (Aula 05 e Aula 06)."""
    if not lista_de_tarefas:
        print("\nNenhuma tarefa cadastrada ainda.")
        return

    print("\n=== LISTA DE TAREFAS CADASTRADAS ===")
    for i, t in enumerate(lista_de_tarefas, start=1):
        print(f"{i}. Título: {t['titulo']} | Data: {t['data']} | Status: {t['status']}")


def filtrar_por_status(lista_de_tarefas):
    """Função para implementar o filtro por status: Feito / Não feito (Aula 02)."""
    print("\n=== FILTRAR TAREFAS ===")
    print("1 - Ver apenas tarefas 'Feito'")
    print("2 - Ver apenas tarefas 'Não feito'")
    opcao = int(input("Escolha o filtro (1 ou 2): "))
    
    status_desejado = "Feito" if opcao == 1 else "Não feito"
    
    print(f"\n--- Tarefas com status: {status_desejado} ---")
    encontrou = False
    
    for t in lista_de_tarefas:
        if t["status"] == status_desejado:
            print(f"- {t['titulo']} (Data: {t['data']})")
            encontrou = True
            
    if not encontrou:
        print("Nenhuma tarefa encontrada com este status.")


# --- PROGRAMA PRINCIPAL (MENU INTERATIVO COM WHILE) ---
def main():
    # Lista para armazenar os dicionários de tarefas (Aula 04 e Aula 06)
    tarefas = []
    
    while True:
        print("\n==============================")
        print("     TO-DO LIST - MENU        ")
        print("==============================")
        print("1 - Cadastrar nova tarefa")
        print("2 - Listar todas as tarefas")
        print("3 - Filtrar tarefas por status")
        print("4 - Sair")
        
        # Tratamento de erros básico para evitar que o programa quebre se o usuário digitar letras (Aula 08)
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("\n[Erro] Digite apenas números inteiros válidos!")
            continue
            
        if opcao == 1:
            nova = cadastrar_tarefa()
            tarefas.append(nova)  # Armazenando na lista (Aula 04)
        elif opcao == 2:
            listar_tarefas(tarefas)
        elif opcao == 3:
            filtrar_por_status(tarefas)
        elif opcao == 4:
            print("\nSaindo do programa. Até mais!")
            break
        else:
            print("\n[Erro] Opção inválida! Escolha entre 1 e 4.")

# Executando o programa
if __name__ == "__main__":
    main()