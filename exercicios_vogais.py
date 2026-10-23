
palavra = input("Digite uma frase: ").lower()
contador = 0

for letra in palavra:
    if letra in "aeiou":
        contador += 1

print(f"Total de vogais: {contador}")