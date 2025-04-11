import math

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('| ' + ' | '.join(linha) + ' |')
    print()

def movimento_valido(tabuleiro, linha, coluna):
    return (0 <= linha < len(tabuleiro) and
            0 <= coluna < len(tabuleiro[0]) and
            tabuleiro[linha][coluna] == ' ')

def chegou_destino(linha, coluna):
    return linha == 1 and coluna == 4

def encontrar_caminho(tabuleiro, linha_atual, coluna_atual, caminho):
    if chegou_destino(linha_atual, coluna_atual):
        caminho.append((linha_atual, coluna_atual))
        return True

    direcoes = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # direita, esquerda, cima, baixo

    for d_linha, d_coluna in direcoes:
        nova_linha = linha_atual + d_linha
        nova_coluna = coluna_atual + d_coluna

        if movimento_valido(tabuleiro, nova_linha, nova_coluna):
            tabuleiro[nova_linha][nova_coluna] = '°'  # marca como visitado
            if encontrar_caminho(tabuleiro, nova_linha, nova_coluna, caminho):
                caminho.append((linha_atual, coluna_atual))
                return True
            tabuleiro[nova_linha][nova_coluna] = ' '  # desmarca (backtracking)

    return False

def main():
    tabuleiro = [
        [' ', ' ', ' ', 'X', 'X'],
        [' ', 'X', ' ', 'X', ' '],
        [' ', 'X', ' ', 'X', ' '],
        [' ', 'X', ' ', ' ', ' ']
    ]
    linha_inicio, coluna_inicio = 3, 0
    caminho = []

    # marca o início
    tabuleiro[linha_inicio][coluna_inicio] = '*'
    #tabuleiro[0][3] = '*'
    mostrar_tabuleiro(tabuleiro)

    if encontrar_caminho(tabuleiro, linha_inicio, coluna_inicio, caminho):
        caminho.append((linha_inicio, coluna_inicio))  # adiciona o início ao final
        caminho.reverse()  # inverte o caminho para ordem do início ao fim

        # limpar tabuleiro e desenhar o caminho final
        for i, linha in enumerate(tabuleiro):
            for j, valor in enumerate(linha):
                if valor == '':
                    tabuleiro[i][j] = '°'
        for linha, coluna in caminho:
            tabuleiro[linha][coluna] = '°'

        print("Caminho encontrado:")
        mostrar_tabuleiro(tabuleiro)
    else:
        print("Não foi possível encontrar um caminho.")

if __name__ == "__main__":
    main()
