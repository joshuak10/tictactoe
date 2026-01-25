class TicTacToe:

    def __init__(self):
        self._board = [[" "] * 3 for j in range(3)]
        self._player = "X"
        self._aiplayer = "O"
        self._currentturn = self._player
        self._state = True
        self._end = ""
        
    
    def loop(self):
        move = input("Move?(row,column)")
        if move == "q":
            self._state = False
        try:
            x,y = move.split(sep = ",")
        except ValueError:
            print("Format: (row,column)")
            return
        y.strip()
        self.mark(int(x),int(y))
        
    def mark(self, i, j):
        if not (0<=i<=2 and 0<=j<=2):
            print("Outside of Bounds")
            return
        if self._board[i][j] != " ":
            print("Occupied Slot")
            return
        
        self._board[i][j] = self._currentturn

        if self._currentturn == self._player:
            self._currentturn = self._aiplayer
        else:
            self._currentturn = self._player
            
    def iswin(self, mark):
        board = self._board
        return (mark == board[0][0]== board[0][1]== board[0][2] or #row 1
            mark == board[1][0]== board[1][1]== board[1][2] or      #row 2
            mark == board[2][0]== board[2][1]== board[2][2] or  #row 3
            mark == board[0][0]== board[1][1]== board[2][2] or  #diagnol
            mark == board[0][2]== board[1][1]== board[2][0] or  #diagnol
            mark == board[0][0]== board[1][0]== board[2][0] or
            mark == board[0][1]== board[1][1]== board[2][1] or
            mark == board[0][2]== board[1][2]== board[2][2]
        )


    def checkstate(self):
        if self._currentturn == self._player:
            winner = self._aiplayer
        else:
            winner = self._player
        if self.checkwin():
            print(f"Winner is {winner}!")
            self._state = False
            self._end = "win"
            return self._end
        
        elif self.checktie():
            print("Tie Game")
            self._end = "tie"
            self._state = False
            return self._end



    def checkwin(self):
         for mark in "XO":
             if self.iswin(mark):
                 return True
         return False
    def checktie(self):
        if not any(" " in row for row in self._board):
            return True
        
    def __str__(self):
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)
    
    #  def minimax(board, depth, isMaximizingPlayer):
    #     winner = 

        