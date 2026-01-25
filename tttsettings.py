class TicTacToe:

    def __init__(self):
        self._board = [[" "] * 3 for j in range(3)]
        self._availablespace = [0,1,2,3,4,5,6,7,8]
        self._player = "X"
        self._aiplayer = "O"
        self._currentturn = self._player
        self._winner = ""
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
        
    def mark(self, i, j, a = None):
        if not (0<=i<=2 and 0<=j<=2):
            print("Outside of Bounds")
            return
        if self._board[i][j] != " ":
            print("Occupied Slot")
            return
        
        if a is None:
            self._board[i][j] = self._currentturn
            self.updatespace(i,j)

            if self._currentturn == self._player:
                self._currentturn = self._aiplayer
            else:
                self._currentturn = self._player
        else:
            self._board[i][j] = a
            
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
        if self.checkwin():
            print(f"Winner is {self._winner}!")
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
                 if mark == "X":
                     self._winner = self._player
                 else:
                     self._winner = self._aiplayer
                 return True
         return False
    def checktie(self):
        if not any(" " in row for row in self._board):
            return True
        
    def __str__(self):
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)
    
    def updatespace(self, i, j):
        index = (i * 3) + (j%3)
        self._availablespace.remove(index)


    
    def minimax(self, depth, isMaximizingPlayer):
        winner = ""
        if self.checkwin():
            winner = self._winner
        if winner == self._aiplayer:
            return 1
        if winner == self._player:
            return -1
        if self.checktie():
            return 0
        
        if isMaximizingPlayer:
            bestscore = float("-inf")
            for each in self._availablespace:
                move_i = each//3
                move_j = each%3
                if self._board[move_i][move_j] != " ":
                    continue
                self.mark(move_i,move_j, self._aiplayer) 
                score = self.minimax(depth+1, isMaximizingPlayer=False)
                self._board[move_i][move_j] = " "
                best_score = max(score, bestscore)
            return best_score
        else:
            bestscore = float("inf")
            for each in self._availablespace:
                move_i = each//3
                move_j = each%3
                if self._board[move_i][move_j] != " ":
                    continue
                self.mark(move_i,move_j, self._player)
                score = self.minimax(depth+1, isMaximizingPlayer=True)
                self._board[move_i][move_j] = " "
                best_score = min(score,bestscore)
            return best_score
        
    def aimove(self):
        best_score = float("-inf")
        best_move = None
        for each in self._availablespace:
            move_i = each//3
            move_j = each%3
            if self._board[move_i][move_j] != " ":
                continue
            self.mark(move_i,move_j,self._aiplayer)
            score = self.minimax(0,False)
            self._board[move_i][move_j] = " "
            if score>best_score:
                best_score = score
                best_move = (move_i, move_j) #dont forget indexes here
        print(best_move)