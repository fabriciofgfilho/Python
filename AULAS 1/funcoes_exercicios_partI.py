#Crie uma função chamada apresentação que receba um nome, idade e curso como.
 
def apresentacao(nome, idade, curso):
    print(f"Olá, {nome}! Você tem {idade} anos e está matriculado no curso de {curso}.")

apresentacao("Fabricio", 39 , "Ford Enter")

#Crie uma função chamada par_ou_impar que receba um número como parâmetro e
#retorne "par" se ele for par e "ímpar" se for ímpar.

def par_ou_impar(n):
    if n % 2 == 0:
        return "Par"
    return "Ímpar"

print(par_ou_impar(10))
print(par_ou_impar(7))
print(par_ou_impar(22))
print(par_ou_impar(15))

#Crie uma função que converta uma temperatura de Fahrenheit para Celsius e para
#Kelvin e print os dois.

def fahr_to_celsius(temp):
    return ((temp - 32) * (5/9))

print(fahr_to_celsius(91.76))  # 33.2
print(fahr_to_celsius(101.3))  # 38.5

celsius = fahr_to_celsius(98.6)
print(celsius)  # 37.0

# Conversão de Celsius para Kelvin: K = C + 273.15
kelvin = celsius + 273.15

print(kelvin)  # 310.15

def converter_temperatura(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    kelvin = celsius + 273.15

    return celsius, kelvin

celsius, kelvin = converter_temperatura(98.6)
print(celsius)
print(kelvin)

#Crie uma função contar_pares(n) que conte e retorne quantos números
#pares existem entre 1 e n (inclusive).

def contar_pares(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count += 1
    return count

print(contar_pares(10))  # 5
print(contar_pares(20))  # 10
print(contar_pares(15))  # 7

# Exercício 6 Crie uma função chamada tamanho_palavra que receba uma string e
#retorne o número de caracteres que ela possui.

def tamanho_palavra(palavra):
    return len(palavra)

print(tamanho_palavra("Python"))  # 6
print(tamanho_palavra("Programação"))  # 11

palavra_digitada = input("Digite uma palavra")
print(tamanho_palavra(palavra_digitada))


#Exercício 7 —Crie uma função eh_primo(n) que retorne True se n for primo e False
#caso contrário. Use for.

def eh_primo(n):
    if n  == 1 or n == 2 or n ==3:
        return True
    else:

        for i in range(2, n):
            if n % i == 0:
                return False
    return True

print(eh_primo(7))   # True
print(eh_primo(10))  # False
print(eh_primo(13))  # Trues
