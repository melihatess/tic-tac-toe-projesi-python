import random

def display_board(board):
    print("+-------+-------+-------+")
    for r in range(3):
        print("|       |       |       |")
        print("|   " + "   |   ".join(str(board[r][c]) for c in range(3)) + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    while True:
        try:
            move = int(input("Hamleni yap (1-9): ").strip())
            if move < 1 or move > 9:
                print("Geçersiz hamle. 1-9 arası bir sayı girmelisiniz.")
                continue
            move -= 1
            row, col = divmod(move, 3)
            if board[row][col] in ('X', 'O'):
                print("Bu kare zaten dolu. Başka bir kare seçin.")
                continue
            board[row][col] = 'O'
            break
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")

def make_list_of_free_fields(board):
    free_fields = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ('X', 'O'):
                free_fields.append((r, c))
    return free_fields

def victory_for(board, sign):
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)):
            return True
        if all(board[j][i] == sign for j in range(3)):
            return True
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    return False

def draw_move(board):
    free = make_list_of_free_fields(board)
    if not free:
        return
    r, c = random.choice(free)
    board[r][c] = 'X'

def count_moves(board):
    return sum(1 for r in range(3) for c in range(3) if board[r][c] in ('X', 'O'))

def main():
    board = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    
    board[1][1] = 'X' 
    print("Oyun başlıyor!")
    display_board(board)

    while True:
        if not make_list_of_free_fields(board):
            print("Berabere!")
            break
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("Kazandın!")
            break

        if not make_list_of_free_fields(board):
            print("Berabere!")
            break
        print("Bilgisayar hamlesini yapıyor...")
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("Bilgisayar kazandı!")
            break

if __name__ == "__main__":
    main()
