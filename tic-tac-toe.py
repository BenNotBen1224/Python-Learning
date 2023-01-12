import random #很tm重要

class TicTacToe:
    ##  之前的代码
    # def __init__(self):
    #     for i in range[3]:
    #         for j in range[3]:
    #             self.board.append('-')
    
    ##  修改后的初始化
    def __init__(self):
        # 创造一个3x3的二维向量
        """
        [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
        """
        self.board = [['-' for j in range(3)] for i in range(3)]
    
    def Player_selection(player):
        if random.randint(0,1) == 0: 
            player = "X" 
        else: player = "O"
    
    def Player_input(self, i, j, player):
        if player == "X":
            x = map(int, input('Where to put your next "X"?').split())
        else:
            x = map(int, input('Where to put yout next "O"?').split())
        self.board[i][j] = x
    
    def Print_board(self):
        print(self.board)