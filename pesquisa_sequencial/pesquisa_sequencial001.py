"""
Programa pesquisa_sequencial
Requisito: Este programa procura um elemento dentro de uma lista Pyton.
Autor: Jessica Caroline Prass
Versão: 0.0.1
Data: 16/08/2022
"""

# Entrada de dados
indice = 0
lista = [1, 2, 3, 7, 8, 9]
numero = int(input("\nDigite o número a procurar: "))
encontrado = False #variavel auxiliar
    
# Programa de dados
while indice < len(lista):
    if lista[indice] == numero:
        encontrado = True
        break
    indice +=1 #varendo toda a lista, não dá bug loop infinito
if encontrado: #True
    print(f"O valor {numero} foi encontrado na posição {indice+1}")
else:
    print(f"O valor {numero} não foi encontrado.")
    
# Saída de dados
