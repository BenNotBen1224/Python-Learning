import random #很tm重要

class TicTacToe:
    ##  修改之前的代码
    # def __init__(self):
    #     for i in range[3]:
    #         for j in range[3]:
    #             self.board.append('-')
    
    def __init__(self):
        # 创造一个3x3的二维向量
        self.board = [['-' for j in range(3)] for i in range(3)]
    
    def Player_input(self, x, player):
        if player == "X":
            x = map(int, input("Where to put your next 'X'?").split())
        else:
            x = map(int, input("Where to put yout next 'O'?").split())
        self.board[x[0]][x[1]] = player
    
    def Check_board(self, player):
        #检查横竖斜是否成功
        if [[self.board[i][j] != player or self.board[j][i] != player or 
             self.board[i][i] != player or self.board[i][3 - i] 
             for j in range(3)] for i in range(3)]:
            win = True
        else:
            win = False
            
        #检查棋子是否满盘
        if[[self.board[i][j] != '-' for j in range[3]] for i in range[3]]:
            win = True
        else:
            win = False
    
    def Game(self, player):
        print("Welcome to the Game")
        print([j, sep=(' ') for j in row] for i in self.board) #为什么不行？
        
        #随机选玩家
        if random.randint(0,1) == 0: 
            player = "X" 
            
        else: player = "O"
        