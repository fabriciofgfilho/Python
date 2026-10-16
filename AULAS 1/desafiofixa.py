#fixação 1#

numero_1 = float(input("Informe o número 1: "))
numero_2 = float(input("Informe o número 2: "))

if numero_1 > numero_2:
        print(f"O número maior é o {numero_1} e o número menor é {numero_2}")

elif numero_1 < numero_2:
        print(f"O número maior é o {numero_2}  e o número menor é {numero_1}")

else:
        print("Os numeros são iguais")

    
#fixação 2#

numero = int(input("Informe um número: "))

if numero == 0:
      print("Numero zerado")

elif numero % 2 == 0:
    print("Numero par")

elif numero % 2 != 0:
    print("Número impar")

else:
      print("Numero zerado")

#fixação 3#

letra = input("Digite a letra incial referente ao estado civil do usuário: ").lower()

#.lower() transforma a variavel em minusculo
#.upper() transforma a variavel em maisculo

if letra == "c":
      print("CASADO")


elif letra == "s":
      print("SOLTEIRO")


elif letra == "d":
      print("DIVORCIADO")

elif letra == "v":
      print("VIUVO")


elif letra == "o":
      print("OUTROS")


else:
      print("DIGITE NOVAMENTE")



      