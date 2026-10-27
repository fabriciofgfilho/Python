#questão 2

contador = 0
soma = 0
while contador < 5:
    soma += contador
    contador += 1
print(soma)

#código ira fazer 5 loops e ir somando os valores na variaveis. Na quinta volta a variavel contador fica = a 5 e o loop é interrupido
# a soma será igual a 10

#questão 3

n = 0
while True:
    n += 3
    if n > 10:
        break
print(n)

#esse é um loop infinito, a cada volta ele ira somar 3 na variavel n e só ira parar quando o valor for maior que 10. por ser um while true
# quando a condição for verdadeira ele executa break e variavel n será de 12.

#questão 4

x = 20
while x > 0:
    x -= 6
    if x < 5:
        break
print(x)

#a cada loop será subtraido 6 da variavel x, q iniciou com 20. temos uma condição de verdade q quando o numero for menor q 5
#o loop encerra. após 3 loops o retorno será 2

#questão5

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Fim")

#variavel i se inicia com 0, vai ter loop até variavel de print do valor da variavel até for = ou maior q 3.
# então imprime 0,1,2 a condição se torna falsa e no else ele imprime o fim tbm
#retorno de 0,1,2,Fim

#questão 7

for i in range(5):
    print(i)

#range()  gera uma sequência numérica. Quando passamos apenas um número (5), ela começa obrigatoriamente do 0
# e vai até o número imediatamente anterior ao limite informado, ou seja, para antes de chegar no 5.

#questão 9

for i in range(10, 0, -4):
    print(i)

#temos um intervalo de 10 para 0, subtraindo 4. teremos 3 voltas de impressão 10 - 6 - 2. para no 2 pois o 0 não é contato.
#se conta 1

#questão 10

palavra = "Python"
cont = 0
for letra in palavra:
    if letra in "aeiou":
        cont += 1
print(cont)

#ira contar as vogais da string "python" - só temos uma o "o"
#imprime 1

#questão 11

texto = "abc"
resultado = ""
for c in texto:
    resultado = c + resultado
print(resultado)

#O loop pega cada letra do texto "abc" e a coloca antes do que já estava acumulado.
#Isso faz com que a string seja invertida (o que era o primeiro caractere passa a ser o último).
#imprime cba

#questão 12

numeros = [3, 8, 5, 10]
total = 0
for n in numeros:
    if n % 2 == 0:
        total += n
print(total)

#soma apenas os numeros pares da lista
#imprime 18.

#questão 13

nomes = ["Ana", "Bia", "Caio", "Davi"]
for nome in nomes:
    if nome == "Caio":
        break
    print(nome)

#imprime até for caio.
#imprime ana e bia

#qestão 14

numeros = [4, 9, 12, 7]
for n in numeros:
    if n > 10:
        print("Achou", n)
        break
else:
    print("Não achou")

#procura na lista numero maior q 10.
#quando achar encerra
#imprime: achou, 12






