
#EXERCICIOS 1
for i in range(2,101,2):
    print(i)
    

#EXERCICIOS 2


geracao_beta = 0
geracao_alfa = 0
geracao_z = 0
millennials = 0
geracao_x = 0
baby_boomers = 0
silent_generation = 0
outros = 0  


quantidade_pessoas = int(input("Informe a quantidade de pessoas (n): "))


for i in range(1, quantidade_pessoas + 1):
    idade = int(input(f"Informe a idade da {i}ª pessoa: "))
    
  
    if 0 <= idade <= 1:
        geracao_beta += 1
    elif 2 <= idade <= 14:
        geracao_alfa += 1
    elif 15 <= idade <= 29:
        geracao_z += 1
    elif 30 <= idade <= 45:
        millennials += 1
    elif 46 <= idade <= 61:
        geracao_x += 1
    elif 62 <= idade <= 80:
        baby_boomers += 1
    elif 81 <= idade <= 101:
        silent_generation += 1
    else:
        outros += 1



print(f"Geração Beta (0 a 1 ano): {geracao_beta}")
print(f"Geração Alfa (2 a 14 anos): {geracao_alfa}")
print(f"Geração Z (15 a 29 anos): {geracao_z}")
print(f"Millennials ou Geração Y (30 a 45 anos): {millennials}")
print(f"Geração X (46 a 61 anos): {geracao_x}")
print(f"Baby Boomers (62 a 80 anos): {baby_boomers}")
print(f"Silent Generation (81 a 101 anos): {silent_generation}")
if outros > 0:
    print(f"Fora das faixas especificadas: {outros}")


#exercicios 3

total_eleitores = int(input("Informe o número total de eleitores: "))


votos_candidato1 = 0
votos_candidato2 = 0
votos_candidato3 = 0


for i in range(total_eleitores):
    print(f"\nEleitor {i + 1}:")
    print("Escolha o seu candidato:")
    print("1 - Candidato A")
    print("2 - Candidato B")
    print("3 - Candidato C")
    
    voto = int(input("Digite o número do seu candidato (1, 2 ou 3): "))
    
  
    if voto == 1:
        votos_candidato1 += 1
    elif voto == 2:
        votos_candidato2 += 1
    elif voto == 3:
        votos_candidato3 += 1
    else:
        print("Voto inválido! Este voto não será contabilizado.")

# Exibindo o resultado final da apuração

print(f"Total de votos para o Candidato A: {votos_candidato1}")
print(f"Total de votos para o Candidato B: {votos_candidato2}")
print(f"Total de votos para o Candidato C: {votos_candidato3}")

