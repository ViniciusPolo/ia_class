import sys

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("| " + " |".join(linha) + " |")

def proximo_movimento(tabuleiro, linha_atual, coluna_atual, profundidade):
    melhor_profundidade = float("inf")
    
    melhor_linha= linha_atual
    melhor_coluna = coluna_atual

    proxima_linha = linha_atual
    proxima_coluna = coluna_atual + 1

    if movimento_valido(tabuleiro, proxima_linha, proxima_coluna):
        if chegou_destino(proxima_linha, proxima_coluna):
            return proxima_linha, proxima_coluna
     
def movimento_valido(tabuleiro, linha, coluna):
    return tabuleiro

def chegou_destino(linha, coluna):
    return linha == 2 and coluna == 2

def main():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    mostrar_tabuleiro(tabuleiro)

    linha_atual = 0
    coluna_atual = 0
    profundidade = 0 



   
    

