"""
Módulo entrada
Requisitos: Este módulo lê dois números digitados pelo usuário.
Autor: Jessica Caroline Prass
Versão: 0.9.1
Data: 23/08/2022
"""

def entra_dados():
    """DOCUMENTANDO O QUE A FUNÇÃO FAZ: Esta função (def) (procedimento, não acumula na memoria) lê dois números digitados pelo usuário, recebe dados."""
    i = 0
    lista_numeros = []
    while i < 2:
        numero = float(input("\nDigite um número: "))
        lista_numeros.append(numero)
        i+=1
    return lista_numeros
    
