import tttsettings

game = tttsettings.TicTacToe()

print(game)

while game._state:
    # if game.checktie() is False:
    #     print("tie game")
    #     break
    game.loop()
    print(game)
    if game.checkstate() == "win" or game.checkstate() == "tie":
        break
    game.aimove()
    print(game)
    if game.checkstate() == "win" or game.checkstate() == "tie":
        break
print("game over!")
