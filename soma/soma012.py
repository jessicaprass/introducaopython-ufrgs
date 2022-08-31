"""
Programa soma
Descrição: Este programa lê dois números digitados pelo usuário, calcula a soma deles
e coloca o resultado na tela.
Autor: Jessica Prass
Versão: 0.1.2
Data: 23/08/2022
"""

# Definição de funções
# subprograma = funções que retorna valor para programa = comando

def entra_dados():
    """DOCUMENTANDO O QUE A FUNÇÃO FAZ: Esta função (def) (procedimento) lê dois números digitados pelo usuário, recebe dados."""
    i = 0
    lista_numeros = []
    while i < 2:
        numero = float(input("\nDigite um número: "))
        lista_numeros.append(numero)
        i+=1
    return lista_numeros
    
def adicao(numero_1, numero_2):
    """Esta função calcula a soma dos números numero_1 e numero_2. Processo os dados"""
    return numero_1 + numero_2

def impressora(soma, numero_1, numero_2):
    """Esta função coloca o resultado da soma do numero_1 com o numero_2 na tela. colocar na tela."""
    print(f"\nA soma do {numero_1} com o {numero_2} é igual a {soma}.")

def main():
    """Esta função controla a execução do programa, chama as funções no momento certo"""
    lista = entra_dados()
    soma = adicao(lista[0], lista[1])
    impressora(soma, numero_1, numero_2)
    
# Execução do programa
main()

