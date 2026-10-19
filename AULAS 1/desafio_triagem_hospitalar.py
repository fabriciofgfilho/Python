#dados do paciente

nome = input("Informe o nome do paciente: ")
idade = int(input("Informe a idade do paciente: "))
sintoma = input("Informe o sintoma principal (ex: dor no peito, falta de ar, febre, etc.): ").lower()

#classificação

if sintoma == "dor no peito" or sintoma == "falta de ar":
    prioridade = "VERMELHA"
elif sintoma == "febre" and idade >= 60:
    prioridade = "AMARELA"
else:
    prioridade = "VERDE"

#emissão da cor da prioridade:

print(f"O paciente {nome} está na prioridade: {prioridade}" )