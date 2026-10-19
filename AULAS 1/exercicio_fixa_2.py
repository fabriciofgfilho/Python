#EXERCICIO 4


idade = int(input("Digite a idade: "))

if (idade >= 16 and idade < 18) or (idade >= 70):

    print(f"SUA IDADE É {idade} ENTÃO SEU VOTO É FACULTATIVO" )

elif idade <16:
    print(f"SUA IDADE É {idade} ENTÃO VC NÃO IDADE PARA VOTAR" )

else:
    print(f"SUA IDADE É {idade} ENTÃO SEU VOTO É OBRIGATORIO" )

#EXERCICIO 5

idade_nadador = int(input("Digite a idade do nadador: "))

if (idade_nadador >= 5 and idade_nadador <= 7):

    print(f"SUA IDADE É {idade_nadador} ENTÃO SUA CATEGORIA É INFANTIL A" )

elif (idade_nadador >= 8 and idade_nadador < 11):
    print(f"SUA IDADE É {idade_nadador} ENTÃO SUA CATEGORIA É INFANTIL B" )

elif (idade_nadador >= 12 and idade_nadador < 13):
    print(f"SUA IDADE É {idade_nadador} ENTÃO SUA CATEGORIA É JUVENIL A" )

elif (idade_nadador >= 14 and idade_nadador < 17):
    print(f"SUA IDADE É {idade_nadador} ENTÃO SUA CATEGORIA É JUVENIL B" )

elif idade_nadador >= 18:
    print(f"SUA IDADE É {idade_nadador} ENTÃO SUA CATEGORIA É ADULTO" )

else:
    print(f"SUA IDADE É {idade_nadador} ENTÃO VOCE AINDA NÃO TEM CATEGORIA" )


#EXERCICIO 6

numero_1 = float(input("Digite o número 1: "))
numero_2 = float(input("Digite o número 2: "))

matematica = (input("Digite qual operação matematica deseja fazer: + = soma, - = subtração, * = multiplicação, / = divisão "))

if matematica == "+":
    print (numero_1+numero_2)

elif matematica == "-":
    print (numero_1-numero_2)

elif matematica == "*":
    print (numero_1*numero_2)

elif matematica == "/" and numero_2 != 0:
    print (numero_1/numero_2)

else:
    print("Refaça")




           


