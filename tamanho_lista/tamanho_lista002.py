"""
Programa tamanho_lista
Requisito: Este programa calcula o tamanho de uma lsta Pyton dada pelo usuário e o coloca na tela.
Autor: Jessica Caroline Prass
Versão: 0.0.2
Data: 16/08/2022
"""

# Entrada de dados
lista = []
while True:
    elemento = input("\nDigite um elemento para a sua lista. Quando encerrar digite X e pressione ENTER.")
    if elemento.upper() == "X":
            break # para encerrar
    lista.append(elemento)
    
# Programa de dados
#calcula tamanho da lista dado pelo usuário
tamanho_lista = len(lista)

# Saída de dados
#colocar o tamanho da lista na tela
print(f"A lista digitada foi {lista} e seu tamanho é {tamanho_lista}.")
