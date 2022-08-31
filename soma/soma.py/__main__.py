"""
Programa soma
Requisitos: Este programa lê dois números digitados pelo usuário, calcula a soma deles
e coloca o resultado na tela.
Autor: Jessica Caroline Prass
Versão: 1.0.0
Data: 23/08/2022
"""

# Importação de módulos

import entrada
import processa
import saida

# Definição de funções
def main():
    """Esta função controla a execução do programa, chama as funções no momento certo"""
    # Entrada
    lista = entrada.entra_dados()

    # Processamento
    soma = processa.adicao(lista[0], lista[1])

    # Saída
    saida.impressora(soma, lista[0], lista[1])
    
# Execução do programa
"""Proteger a função"""
if __name__ == "__main__": """padrão"""
   main()

