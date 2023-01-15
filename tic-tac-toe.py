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
        
    def Print_board(self):
        # print([[(j, sep=(' ')) for j in row] for i in self.board)
            # 为什么不行？
            # sep 似乎只能在纯print里使用，不能这么操作。而且，你要用两个[],你这里调动了两个loop。最后，这种操作最好是define的时候用，print就别偷懒了
        for vertical in self.board:
                for horizontal in vertical:
                    print(horizontal, end=" ")
                print("\n")
            
    def Check_board_win(self, player):
        #检查横竖斜是否成功
        for i in range(3):
            if len([True for j in range(3) if self.board[i][j] == player]) == 3:
                return True 
            elif len([True for j in range(3) if self.board[j][i] == player]) == 3:
                return True
            elif len([True for j in range(3) if self.board[j][j] == player]) == 3:
                return True
            elif len([True for j in range(3) if self.board[j][2 - j] == player]) == 3:
                return True
        return False
        
    def Check_board_filled(self):
        #检查棋子是否满盘1
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    return False
        return True

    def Game(self):
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
        #初始化棋盘和玩家
        self.board = [['-' for j in range(3)] for i in range(3)]
        player = "X" if random.randint(0, 1) == 0 else "O"
        self.Print_board()
        print("Welcome to Game!")
        
        while True:
            #提示玩家输入
            x = list(map(int, input(f"Player {player} turn" + "(please type in x and y position using comma in between):").split(",")))
            if self.board[x[0] - 1][x[1] - 1] == '-':
                self.board[x[0] - 1][x[1] - 1] = player
            else:
                while self.board[x[0] - 1][x[1] - 1] != '-':
                    x = list(map(int, input(f"Space already occupied" + "(please type in another x and y position using comma in between):").split(",")))
                self.board[x[0] - 1][x[1] - 1] = player

            ##上传玩家输出
            self.Print_board()
            
            #检查结果
            if self.Check_board_win(player) == True:
                print(f"Congratulations Player {player}, you win the Game!")
                return False
            if self.Check_board_filled() == True and self.Check_board_win(player) == False:
                print("Draw\nBoard is filled")
                return False
                
            #玩家互换
            # player = "X" if player == "O" else player = "O"
            # 应该这样做
            player = "X" if player == "O" else "O"
            
A_Game = TicTacToe()
A_Game.Game()
                  
            
        
        
            
        
