class TicTacToe:

    def __init__(self):
        self._board = [[" "] * 3 for j in range(3)]
        self._player = "X"
        
    
    def mark(self, i, j):
        if not (0<=i<=2 and 0<=j<=2):
            raise ValueError("Outside of Board")
        if self._board[i][j] != " ":
            raise ValueError("Board Position Occupied")
        if self.winner() is not None:
            raise ValueError("Game Completed")
        if self.winner() == "Tie":
            raise ValueError("Game Tied")
        self._board[i][j] = self._player
        if self._player == "X":
            self._player = "O"
        else:
            self._player = "X"
    def iswin(self, mark):
        board = self._board
        return (mark == board[0][0]== board[0][1]== board[0][2] or
            mark == board[1][0]== board[1][1]== board[1][2] or
            mark == board[2][0]== board[2][1]== board[2][2] or
            mark == board[0][0]== board[1][1]== board[2][2] or
            mark == board[2][0]== board[1][1]== board[0][2] or
            mark == board[0][0]== board[1][0]== board[2][0] or
            mark == board[0][1]== board[1][1]== board[2][1] or
            mark == board[0][2]== board[1][2]== board[2][2]
        )
    def winner (self):
        for mark in "XO":
            if self.iswin(mark):
                return mark
            if not any(" " in row for row in self._board):
                return "Tie"
            return None
        
    def __str__(self):
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)

        


