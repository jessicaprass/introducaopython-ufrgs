"""
Programa repete_numero
Requisitos: Este programa lê um numero do teclado do usuário e o repete na tela 10 vezes. 10, igual a 10 ou menor que 10.
Autor: Jessica Caroline Prass
Versão: 0.0.3 = resolve bug loop infinito com i = i + 1 ou i += 1
Data: 11/08/2022
"""

# Entrada de dados
# Ler número de teclado
numero = float(input("\nDigite um número: "))
i = 0

# Programa de dados

# Saída de dados
# Imprimir na tela 10 vezes
while i < 10:
    print(f"O número digitado pelo usuário foi {numero}.")
    i += 1

