"""
Programa tamanho_lista
Requisito: Este programa calcula o tamanho de uma lsta Pyton dada pelo usuário e o coloca na tela.
Autor: Jessica Caroline Prass
Versão: 0.0.1
Data: 16/08/2022
"""

# Entrada de dados
#entrada pelo usuário
lista = []
while True: # verdade, para escapar do laço while, condição para comando break, interrompe o laço
    elemento = input("Digite um elemento para a sua lista. Quando encerrar digite X e pressione ENTER.")
    if elemento == "X":
            break # para encerrar
    lista.append(elemento)
    
# Programa de dados
#calcula tamanho da lista dado pelo usuário
tamanho_lista = len(lista)

# Saída de dados
#colocar o tamanho da lista na tela
print(f"\nO tamanho da lista digitada é {tamanho_lista}.")
