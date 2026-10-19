#Entrada do salário atual e a gradedor
salario_atual = float(input("Informe o salário do funcionario: "))
grade = input("Informe a grade do funcionario (B ou C): ").upper()


salario_minimo = 1621.00

percentual = 0.0

# Regras de Reajuste
if grade == 'B':
    if salario_atual == salario_minimo:
        percentual = 4.14
    elif salario_minimo < salario_atual < (3 * salario_minimo):
        percentual = 8.24
    elif (3 * salario_minimo) <= salario_atual < (6 * salario_minimo):
        percentual = 16.48
    else:
        print("Salário não entra na Grade B.")
        exit()

elif grade == 'C':
    if salario_minimo <= salario_atual < (3 * salario_minimo):
        percentual = 10.0
    elif (3 * salario_minimo) <= salario_atual < (6 * salario_minimo):
        percentual = 16.48
    elif (6 * salario_minimo) < salario_atual < (8.5 * salario_minimo):
        percentual = 20.0
    elif salario_atual >= (8.5 * salario_minimo):
        percentual = 28.0
    else:
        print("Salário não entra na Grade C.")
        exit()
else:
    print("Grade inválida!")
    exit()


valor_aumento = salario_atual * (percentual / 100)
novo_salario = salario_atual + valor_aumento

#RELATORIOFINAL
print("Relatório de Reajuste Salarial" )
print(f"Salário antes do reajuste: R$ {salario_atual}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {valor_aumento}")
print(f"Novo salário, após o aumento: R$ {novo_salario}")