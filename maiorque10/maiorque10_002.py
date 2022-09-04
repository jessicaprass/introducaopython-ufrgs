"""
Programa maiorque10
Descrição/Requisitos: Este programa imprime na tela uma frase que diz "se o número digitado pelo usuário é maior que 10, menor que ou igual a 10".
Autor: JessicCaroline Prass
Versão: 0.0.2
Data: 11/08/2022
"""

# Entrada de dados
# Usuário digita dados
numero = float(input("\nDigite um número: "))
frase = "Este número não é maior do que 10."

# Programa de dados
#Descobrir se o número é maior que 10
#Estrutura de controle de fluxo de execução SELEÇÃO
if numero > 10:
        frase = "Este número é maior que 10."

# Saída de dados
# Programa imprime na tela
print(frase)
