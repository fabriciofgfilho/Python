#CALCULADORADETROCOS#

a = float(input("DIGITE O VALOR DA COMPRA: "))
b = float(input("DIGITE O VALOR PAGO: "))

troco = (b-a)

print(f"Sua compra deu {a} e voce pagou {b}, sendo assim seu troco é de {troco}")


#CONVERSOR DE SEGUNDOS#

c = int(input("DIGITE QUANTOS SEGUNDOS DESEJA CONVERTER: "))

horas = c / 3600
minutos = c / 60

print(f"O valor de segundos inseridos em horas é {horas}, em minutos é {minutos}, e em segundos é {c}")


#CALCULO DE IMC#

d = float(input("DIGITE SEU PESO: "))
                   
e = float(input("DIGITE SUA ALTURA: "))

imc = {d / (e * e)}

print(f"Seu Índice de Massa Corporal é de {imc}")

#AUMENTO DE SALÁRIO#

f = float(input("SALARIO ATUAL DO FUNCIONÁRIO: "))
                   
g = int(input("QUAL PORCENTAGEM DE AUMENTO SERÁ APLICADA: "))

h = f*(g/100)

salario_novo = (f + h)


print(f"O valor do aumento do salário do funcionário será de {h}, sendo a assim o novo salário será de {salario_novo}")

#CONSUMO MÉDIO DE COMBUSTIVEL#

i = float(input("QUAL FOI A DISTANCIA PERCORRIDA DO VEÍCULO EM KM? "))
                   
j = float(input("QUANTOS LITROS DE COMBUSTIVEL FOI CONSUMIDO NESSE PERCURSO? "))

h = i/j


print(f"O CONSUMO MÉDIO DO VÉICULO É DE {h} LITROS DE COMBUSTIVEL POR KM RODADO")







