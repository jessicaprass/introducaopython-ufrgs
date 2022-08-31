"""
Programa soma
Descrição: Este programa soma dois números dados pelo usuário e imprime.
Autor: Jessica Prass
Versão: 0.0.5 # bug quando utilizado número com vírgula
Data: 09/08/2022
"""

# Entrada de dados
#input = entende que é texto, permite fazer a leitura do teclado do usuário durante execução programa 
#função float = transforma texto/string em número
#função int = transforma string em número inteiro. vai dar erro se usuário entrar com número com virgula
numero_1 = int(input("Entre a primeira parcela."))
numero_2 = int(input("Entre a segunda parcela."))

# Processamento de dados
soma = numero_1 + numero_2 

# Saída de dados
print(f"O resultado da soma do {numero_1} com o {numero_2} é igual a {soma}.")
