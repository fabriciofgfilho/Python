

print("TO DO LIST")
n = int(input("Informe a quantidade de atividades que deseja cadastrar: "))


total_profissional = 0
total_pessoal = 0


urgente = 0
moderado = 0
normal = 0


executando = 0
agendado = 0
ignorado = 0
concluido = 0
impedido = 0


for i in range(n):
    print(f"\n--- Cadastro da Atividade {i + 1} de {n} ---")
    
    
    print("Tipo da Categoria")
    print("1 - Profissional")
    print("2 - Pessoal")
    opcao_cat = int(input("Escolha o tipo da categoria (1 ou 2): "))
    
    if opcao_cat == 1:
        escopo = "Profissional"
        total_profissional += 1
    else:
        escopo = "Pessoal"
        total_pessoal += 1
        
   
    categoria = input("Informe o título da categoria (ex: Trabalho, Estudos, Doméstico): ")

    atividade = input("Descreva a atividade de forma breve: ")
    
    # 4. Status da Atividade
    print("\nStatus da Atividade:")
    print("1 - Executando")
    print("2 - Agendado")
    print("3 - Ignorado")
    print("4 - Concluído")
    print("5 - Impedido")
    op_status = int(input("Escolha o status (1 a 5): "))
    
    if op_status == 1:
        status = "Executando"
        executando += 1
    elif op_status == 2:
        status = "Agendado"
        agendado += 1
    elif op_status == 3:
        status = "Ignorado"
        ignorado += 1
    elif op_status == 4:
        status = "Concluído"
        concluido += 1
    else:
        status = "Impedido"
        impedido += 1
        
    
    print("\nRelevância da Atividade:")
    print("1 - Urgente")
    print("2 - Moderado")
    print("3 - Normal")
    op_relevancia = int(input("Escolha a relevância (1 a 3): "))
    
    if op_relevancia == 1:
        relevancia = "Urgente"
        urgente += 1
    elif op_relevancia == 2:
        relevancia = "Moderado"
        moderado += 1
    else:
        relevancia = "Normal"
        normal += 1
        
    print(f">> Atividade '{atividade}' registrada com sucesso!")

# Exibindo o relatório consolidado ao final

print("\nRELATÓRIO FINAL DE ATIVIDADES    ")

print(f"Total de atividades cadastradas: {n}")
print(f"- Profissional: {total_profissional}")
print(f"- Pessoal: {total_pessoal}")

print("\nTotal por Relevância")
print(f"Urgente: {urgente}")
print(f"Moderado: {moderado}")
print(f"Normal: {normal}")

print("\nTotal por Status")
print(f"Executando: {executando}")
print(f"Agendado: {agendado}")
print(f"Concluído: {concluido}")
print(f"Ignorado: {ignorado}")
print(f"Impedido: {impedido}")
