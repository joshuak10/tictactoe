import tttsettings

game = tttsettings.TicTacToe()

print(game)

while game._state:
    if game.checktie() is False:
        print("tie game")
        break
    move = input("Move?(row,column)")
    if move == "q":
        break
    x,y = move.split(sep = ",")
    y.strip()
    game.mark(int(x),int(y))
    print(game)
    if game.checkwin():
        print("Winner!")
        break
print("game over!")
#TEST GIT SAVE STATE 10"
# return (mark == board[0][0]== board[0][1]== board[0][2] or #row 1
#             mark == board[1][0]== board[1][1]== board[1][2] or      #row 2
#             mark == board[2][0]== board[2][1]== board[2][2] or  #row 3
#             mark == board[0][0]== board[1][1]== board[2][2] or  #diagnol
#             mark == board[0][2]== board[1][1]== board[2][0] or  #diagnol
#             mark == board[0][0]== board[1][0]== board[2][0] or
#             mark == board[0][1]== board[1][1]== board[2][1] or
#             mark == board[0][2]== board[1][2]== board[2][2]