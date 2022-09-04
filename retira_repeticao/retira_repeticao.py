"""
Programa retirao_repeticao
Requisitos: Dada uma lista de dados do usuário, retire todos os dados repetidos.
Coloque na tela a lista sem repetição.
Autor: Jessica Caroline Prass
Versão: 0.0.1
Data: 18/08/2022
"""

# Entrada de dados
# Leitura de lista de dados do usuário
lista = []
resultado_lista = []

while True:
    elementos = input("\nDigite elementos da sua lista. Ou, digite X para encerrar. ")
    if elementos == elementos.upper() == "X":
        break
    lista.append(elementos)

# Processamento de dados
# Retire todos os dados repetidos
#for elementos in lista:
#    if elementos not in resultado_lista:
#        resultado_lista.append(elementos)

#i = 0
#while i < len(lista):
#   j = i + 1
#while j < len(lista):
#   if lista[j] == lista[i]:
#       lista.pop(j)
#       j+=1
#       i+=1

#PYTONICO dupla interação
for i in list(range(len(lista) - 2)): #se 10 elementos - 2 = 8 (inicio em 0 vai até 7)
    for j in list(range(len(lista) - 2)):
        if lista [j] == lista[j + 1]:
            del lista[j + 1]
            
# Saída de dados
# Colocar na tela a lista sem repetição.
#print(f"\n A lista sem numeros repetidos é: {resultado_lista}")

#print(f"Os elementos digitados sem repetição foram: {lista}")

print(f"A lista sem repetição é {lista}")
