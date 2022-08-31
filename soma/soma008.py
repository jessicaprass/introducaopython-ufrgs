"""
Programa soma
Requisitos: Este programa lê dois números do teclado, calcula a sua soma e imprime na tela o resultado.
Autor: Jessica Prass
Versão: 0.0.8
Data: 11/08/2022
"""

# Entrada de dados
i = 0
while i < 2:
    numero = float(input("\nDigite um número: "))
    i += 1

# Programa de dados
resultado = numero + numero

# Saída de dados
print(f"O soma dos número digitados é {resultado}.")

