import math
from random import randrange as r


# Tabuleiro representado como lista de 9 elementos
board = [" " for _ in range(9)]

def print_board():
    for i in range(3):
        print(board[i*3:(i+1)*3])

def check_winner(b):
    win_combos = [
        [0,1,2], [3,4,5], [6,7,8], # linhas
        [0,3,6], [1,4,7], [2,5,8], # colunas
        [0,4,8], [2,4,6]           # diagonais
    ]
    for combo in win_combos:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] != " ":
            return b[combo[0]]
    if " " not in b:
        return "Empate"
    return None

def minimax(b, is_maximizing, depth):
    winner = check_winner(b)
    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    elif winner == "Empate" or depth == 0:
        return 0  # empate ou profundidade máxima

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, False, depth - 1)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, True, depth - 1)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move(max_depth=3):  # você pode ajustar isso para 1, 2, 3...
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, False, max_depth)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move
# Loop do jogo
print("Você é 'O'. IA é 'X'.")
level = int(input("Escolha seu level (1-Fácil, 2-Médio, 3-Difícil): "))
if level == 1:
    level = r(1, 3)
elif level == 2:
    level = r(4, 6)
elif level == 3:
    level = r(7, 9)
while True:
    print_board()
    # Jogador humano
    pos = int(input("Escolha sua posição (0-8): "))
    if board[pos] != " ":
        print("Posição ocupada. Tente de novo.")
        continue
    board[pos] = "O"

    if check_winner(board):
        break

    # Jogada da IA
    ia_move = best_move(level)
    board[ia_move] = "X"

    if check_winner(board):
        break

# Resultado final
print_board()
resultado = check_winner(board)
if resultado == "Empate":
    print("Deu empate!")
else:
    print(f"{resultado} venceu!")
