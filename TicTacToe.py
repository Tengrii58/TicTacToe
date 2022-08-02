class ttt:
    def __init__(self):
        self.board = []
    def c_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)
    def s_board(self):
        for i in self.board:
            for j in i:
                print(j,end="")
            print()
    def player(self):
        return True
    def player_change(self,player1):
        if player1 == "X":
            return True
        else:
            return False
        
    def winner(self, player):
        win = none
        n = len(board)
        
        #This will check the columns
        for i in range (n)
            win = True
            for j in range(n):
                if board[i][j] != player
                    win = false
                    break
        if win:
            return win
        
        #Rows


        #Diagonal

    def mark(self,row,clm,player):
        self.board[row][clm] = player


    def start(self):
        self.c_board()
        player1 = " "
        if self.player() == True:
            player1 = "X"
        else:
            player1 = "O"

        while True:
            print("Player {} Turn".format(player1))

            self.s_board()

            row, clm = list(
                map(int,input("sayı:").split()))
            print()

            self.mark(row -1,clm -1,player1)
            if self.player_change(player1):
                player1 = "O"
            else:
                player1 = "X"

q = ttt()
q.start()


