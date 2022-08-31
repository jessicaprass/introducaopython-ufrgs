"""
Programa soma
Requisitos: Este programa lê dois números do teclado, calcula a sua soma e imprime na tela o resultado.
Autor: Jessica Prass
Versão: 0.0.6
Data: 11/08/2022
"""

# Entrada de dados
numeros = [] # cria uma lista de números vazia.
i = 0 # contador = variável para contar quantos números foram digitados.

while i < 2:
    numeros.append( # .append = adiciona próximo número
        float(
            input("Entre um núemero: ")
            )
        )
    i += 1

# Programa de dados
soma = numeros[0] + numeros[1]

# Saída de dados
print(f"O resultado da soma do {numeros[0]} com o {numeros[1]} é igual a {soma}.")

