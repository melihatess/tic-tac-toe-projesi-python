from random import randrange

def DisplayBoard(board):

    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(board[0][0]) + "   |   " + str(board[0][1]) + "   |   " + str(board[0][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(board[1][0]) + "   |   " + str(board[1][1]) + "   |   " + str(board[1][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + str(board[2][0]) + "   |   " + str(board[2][1]) + "   |   " + str(board[2][2]) + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def EnterMove(board):

    while True:
        try:
            move = int(input("Hamleni yap (1-9): "))

            if move < 1 or move > 9:
                print("Geçersiz hamle. 1-9 arası bir sayı girmelisiniz.")
                continue

            move -= 1 
            row = move // 3
            col = move % 3
            
            if board[row][col] == 'X' or board[row][col] == 'O':
                print("Bu kare zaten dolu. Başka bir kare seçin.")
            else:
                board[row][col] = 'O'
                break 
                
        except ValueError:
            print("Geçersiz giriş. Lütfen bir sayı girin.")

def MakeListOfFreeFields(board):

    free_fields = []
    for r in range(3):
        for c in range(3):
            if board[r][c] != 'X' and board[r][c] != 'O':
                free_fields.append((r, c))
    return free_fields

def VictoryFor(board, sign):

    for r in range(3):
        if board[r][0] == sign and board[r][1] == sign and board[r][2] == sign:
            return True

    for c in range(3):
        if board[0][c] == sign and board[1][c] == sign and board[2][c] == sign:
            return True

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    return False

def DrawMove(board):

    free = MakeListOfFreeFields(board)
    if len(free) > 0:
        index = randrange(len(free))
        row, col = free[index]
        board[row][col] = 'X'

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

board[1][1] = 'X'
moves_made = 1 

print("Oyun başlıyor!")
DisplayBoard(board)

while moves_made < 9:
    EnterMove(board)
    moves_made += 1
    DisplayBoard(board)

    if VictoryFor(board, 'O'):
        print("Kazandın!")
        break

    if moves_made == 9:
        print("Berabere!")
        break

    print("Bilgisayar hamlesini yapıyor...")
    DrawMove(board)
    moves_made += 1
    DisplayBoard(board)

    if VictoryFor(board, 'X'):
        print("Bilgisayar kazandı!")
        break
