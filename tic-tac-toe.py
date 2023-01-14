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
    
    def Check_board_win(self, player):
        #检查横竖斜是否成功
        if [[self.board[i][j] != player or self.board[j][i] != player or 
             self.board[i][i] != player or self.board[i][3 - i] 
             for j in range(3)] for i in range(3)]:
            win = True
        else:
            win = False
            
    def Check_board_filled(self):
        #检查棋子是否满盘
        if[[self.board[i][j] != '-' for j in range[3]] for i in range[3]]:
            win = True
        else:
            win = False
    
    def Game(self, x, player):
        """
        印出九宫格
        选择玩家
        代入玩家输入
        重新显示新九宫格
        检查棋局状态
        替换玩家
        代入玩家输入
        重新显示九宫格
        检查棋局状态......
        赢/输
        上局未开头玩家下局开头
        """
        print("Welcome to Game")
        
        while True:
            print([(j, sep=(' ')) for j in row] for i in self.board) 
            #为什么不行？
        
            #随机选玩家并提示下棋
            if random.randint(0,1) == 0: 
                player = "X" 
            else: 
                player = "O"
            print(f"Player {player} turn")
        
            ##上传玩家输出
            self.board[x[0]][x[1]] = player
            
            #检查结果
            self.Check_board()
            
            if self.Check_board_win(player):
                print(f"Congradulations Player {player}, you win the Game!")
                False
        
            if self.Check_board_filled():
                print("Draw \n Board is filled")
                False
                
            #玩家互换
            player = "X" if player == "O" else player = "O"

A_Game = TicTacToe()
A_Game.Game()
                  
            
        
        
            
        