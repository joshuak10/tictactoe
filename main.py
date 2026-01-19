import tttsettings

game = tttsettings.TicTacToe()

print(game)

while True:
    move = input("Move?(row,column)")
    if move == "q":
        break
    x,y = move.split(sep = ",")
    y.strip()
    game.mark(int(x),int(y))
    print(game)
    