"""
Programa distingue_numero
Requisitos: Este programa imprime na tela uma frase dizendo se o número digitado pelo usuário é maior que 10, igual a 10 ou menor que 10.
Autor: Jessica Caroline Prass
Versão: 0.0.1
Data: 11/08/2022
"""

# Entrada de dados
# Usuário digita dados
numero = float(input("\nDigite um número: "))

# Programa de dados
#Descobrir se o número é maior que 10, igual a 10 ou menor que 10
#Estrutura de controle de fluxo de execução SELEÇÃO
if numero > 10:
    frase = "Este número é maior que 10."
elif numero == 10:
    frase = "Este número é igual a 10."
else:
    frase = "Este número é menor que 10."
    
# Saída de dados
# Programa imprime na tela
print(frase)
