#exemplo 1

letra = ["a", "b", "c", "d", "e", "f"]
print(f"tamanho da lista: {len(letra)}")
print(f"endereço da letra f: {letra.index("f")}")


#exemplo 2

letras = ["a", "b", "c", "d","e","f"]
var = input("informe uma letra: ")
if var.lower() in letras:
    print(f"A Letra '{var. lower()}' está na lista")
else:
    print(f"A Letra '{var.lower()}' NÃO esta na lista")