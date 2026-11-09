# Exercício 8 - crie uma função chamada preço_final que recebe preço e a poarcentagem de desconto do 
#produtoe calcule o valor a ser pago

def preço_final(preço, desconto):
    return preço - (preço * desconto)


print(preço_final(100, 0.2))  # 80.0
print(preço_final(50, 0.1))   # 45.0
print(preço_final(200, 0.3))  # 140.0

# exercicio 9 -receber uma nota e ser for >=7 aprovado, de 5 até 6.9 em recuperação e baixo de 5 reprovado.
nota1 = float(input("digite uma nota"))

def situação_nota(nota1):
  
    if nota1 >= 7: 
        print("Aprovado")
    elif nota1 >= 5 or nota1 <= 6.9:
        print("Em Recuperação")
    else:
        print("Reprovado")


#exercicio 10 - 



numero = int (input("Entre com numero que será analisado"))

def analise_numero1(numero):
    if numero % 2 == 0:


def analise_numero1(numero):
    if numero > 0
        return "positivo"
    elif numero == 0
        return "zerado"
    else :
        return "negativo"
print (analise_numero(0))   # "zerado"
print (analise_numero(-3))  # "negativo"
print (analise_numero(5))   # "positivo"