import random
import keyboard

class RockPaperScissors:
    
    def __init__(self):
        print("Welcome to Game!")
    
    def Check_Who_Wins(self, player1, player2):
        List = ["Rock", "Paper", "Scissor"]
        
    def Game(self):
        
        self.__init__()
        
        #记录玩家输入
        player1 = 'X' if random.randint(0, 1) == 0 else 'Y'
        A = input("{player1}'s turn (make sure no other player is watching):")
        player2 = 'X' if player1 == 'Y' else 'X'
        B = input("{player2}'s turn (make sure no other player is watching):")
        
        #显示玩家输入
        print(A + "Vs." + B)
        if keyboard.is_pressed(' '):
           Check_Who_Wins(self, player1, player2)
            
        
    """
    随机挑选玩家
    提示并记录玩家输入
    X Vs. Y
    判断输赢
        如赢，结束游戏
        如输，继续游戏
    输出结果
    """