# O programa manipula uma lista de compras mostrando o resultado passo a passo
compras = ["arroz", "feijao", "cafe"]
print("Inicial:", compras)
compras.append("acucar")
print("Apos append('acucar'):", compras)
compras.insert(1, "leite")
print("Apos insert(1, 'leite'):", compras)
compras.remove("feijao")
print("Apos remove('feijao'):", compras)
print("Quantidade final de itens:", len(compras))


# O programa demonstra o uso e imutabilidade de tuplas
cidades = ("Sao Paulo", "Campinas", "Santos", "Sorocaba")
print("Segunda cidade:", cidades[1])
print("Fatia (2a e 3a):", cidades[1:3])
# cidades[0] = "Rio de Janeiro"
# Erro: TypeError: 'tuple' object does not support item assignment
lista_cidades = list(cidades)
lista_cidades.append("Jundiai")
cidades = tuple(lista_cidades)
print("Tupla atualizada:", cidades)

# O programa manipula dados de um dicionario representando um aluno
aluno = {"nome": "Lucas", "idade": 20, "curso": "Python"}
print("Inicial:", aluno, "Tamanho:", len(aluno))
aluno["nota"] = 9.5
print("Apos adicionar nota:", aluno, "Tamanho:", len(aluno))
aluno["idade"] = 21
print("Apos atualizar idade:", aluno, "Tamanho:", len(aluno))
del aluno["curso"]
print("Apos remover curso:", aluno, "Tamanho:", len(aluno))


# O programa percorre um catalogo de produtos e encontra o mais caro
produtos = {"Caneta": 2.50, "Caderno": 15.00, "Mochila": 80.00, "Estojo": 12.00, "Regua":
4.00}
produto_mais_caro = ""
preco_mais_caro = 0.0
for prod, preco in produtos.items():
print(f"{prod}: R$ {preco:.2f}")
if preco > preco_mais_caro:
preco_mais_caro = preco
produto_mais_caro = prod
print(f"\nProduto mais caro: {produto_mais_caro} (R$ {preco_mais_caro:.2f})")