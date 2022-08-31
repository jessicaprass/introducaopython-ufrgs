"""
Programa soma
Descrição: Este programa soma dois números dados pelo usuário e imprime.
Autor: Jessica Prass
Versão: 0.0.4 # corrigindo bug soma
Data: 09/08/2022
"""

# Entrada de dados
#input = entende que é texto, permite fazer a leitura do teclado do usuário durante execução programa
#função float = transforma texto/string em número
numero_1 = float(input("Entre a primeira parcela."))
numero_2 = float(input("Entre a segunda parcela."))

# Processamento de dados
soma = numero_1 + numero_2

# Saída de dados
print(f"O resultado da soma do {numero_1} com o {numero_2} é igual a {soma}.")
