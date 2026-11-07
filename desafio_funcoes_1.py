#desafio1


def bhaskara(a, b, c):
    # 1. Calcular o valor de Δ (delta)[cite: 3]
    delta = (b ** 2) - (4 * a * c)
    
    # 2. Se Δ for menor que zero -> exibir mensagem de erro[cite: 3]
    if delta < 0:
        print("A equação não possui raízes reais")
        
    # 3. Se Δ for maior ou igual a zero -> calcular e exibir as duas raízes[cite: 3]
    else:
        x1 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b - (delta ** 0.5)) / (2 * a)
        print(f"Raízes: {x1} e {x2}")

# Exemplos de teste fornecidos:
bhaskara(1, -5, 6)  # Deve retornar raízes 3 e 2[cite: 3]
bhaskara(1, 2, 5)   # Deve retornar "sem raízes reais"[cite: 3]

#desafio2


def verificar_evento(ano):
    # Copa do Mundo ocorre em anos como 2018, 2022, 2026 (resto 2 ao dividir por 4)
    if ano % 4 == 2:
        return f"Em {ano} tem Copa do Mundo!"
    
    # Olimpíadas de Verão ocorrem em anos como 2021, 2024, 2028
    elif ano % 4 == 0 or ano == 2021:
        return f"Em {ano} tem Olimpíadas de Verão!"
    
    else:
        return f"Em {ano} não há Copa do Mundo nem Olimpíadas de Verão."

# Ciclo While True para testar vários anos consecutivamente
while True:
    entrada = input("Digite um ano (ou digite 'sair' para encerrar): ")
    
    if entrada.lower() == 'sair':
        print("A encerra o programa. Até logo!")
        break
        
    # Converte a entrada para número inteiro
    ano_usuario = int(entrada)
    
    # Chama a função e exibe o resultado
    resultado = verificar_evento(ano_usuario)
    print(resultado)
    print("-" * 40)