#CONSUMO MÉDIO DE COMBUSTIVEL#

a = int(input("QUAL FOI A DISTANCIA TOTAL DA VIAGEM EM KM? "))
                   
b = float(input("QUAL CONSUMO MÉDIO DO VÉICULO EM KM POR LITRO DE COMBUSTIVEL? "))

c = float(input("QUAL VALOR ATUAL DO LITRO D0 COMBUSTIVEL? "))

d = float(input("QUAL SERÁ O CUSTO DE PEDAGIO DURANTE A VIAGEM "))

e = int(input("QUANTAS PESSOAS IRÃO NA VIAGEM "))

gasto_combustivel = (a / b)

custo_total_combustivel = (gasto_combustivel * c)

custo_total_viagem = (custo_total_combustivel + d)

custo_total_por_pessoa = (custo_total_viagem / e)



print(f"SERÃO GASTOS {gasto_combustivel} LITROS DE COMBUSTIVEL, SENDO O CUSTO TOTAL DE COMBUSTIVEL DE {custo_total_combustivel}.")

print(f"O TOTAL DE CUSTO DA VIAGEM SERÁ DE {custo_total_viagem} E CADA PESSOA IRÁ GASTAR O TOTAL DE {custo_total_por_pessoa}.")

print("BOA VIAGEM")





