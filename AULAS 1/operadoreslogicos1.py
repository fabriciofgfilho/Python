#Exemplo do uso de Operadores Lógicos:


#O Operador OR:

tem_bone = input("Você está usando boné? S - Sim, N - Não ")
tem_camisa_azul = input("Você está usando uma camisa azul? S - Sim, N - Não ")
idade = int(input("Informe sua idade: "))

if tem_bone == "S" or tem_camisa_azul == "S":
    print("Entrou porquê ou usa bone ou usa camisa azul.")
else:
    print("Não entrou")

#O Operador AND:

tem_bone = input("Você está usando boné? S - Sim, N - Não ")
tem_camisa_azul = input("Você está usando uma camisa azul? S - Sim, N - Não ")
idade = int(input("Informe sua idade: "))

if tem_bone == "S" and tem_camisa_azul == "S":
    print("Entrou porquê usa bone e usa camisa azul.")
else:
    print("Não entrou")

#O Operador not:

tem_bone = input("Você está usando boné? S - Sim, N - Não ")
tem_camisa_azul = input("Você está usando uma camisa azul? S - Sim, N - Não ")
idade = int(input("Informe sua idade: "))

if tem_bone == "S" and tem_camisa_azul == "S" and (not idade < 18):
    print("Entrou porquê usa bone e usa camisa azul e não é menor que 18 anos.")
else:
    print("Não entrou")