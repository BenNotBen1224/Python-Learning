import random
import keyboard

class RockPaperScissors:
    
    def __init__(self):
        
        self.List = ["Rock", "Paper", "Scissor"]
    
    def Check_Who_Wins(self, player1, player2):
        
        
        for i in range(2):
            if(player1 == self.List[i+1] and player2 == self.List[i]):
                print("Player 1 Wins!")
                break
            if(player1 == self.List[i] and player2 == self.List[i+1]):
                print("Player 2 Wins!")
                break
            else:
                print("Draw, play again.")
                player1 = player2 = ''

        """
        if((player1 == "Rock" and player2 == "Scissor") or
           (player1 == "Scissor" and player2 == "Paper") or
           (player1 == "")
           )
           """
        
    def Game(self):
        """
        随机挑选玩家
        提示并记录玩家输入
        X Vs. Y
        判断输赢
            如输、赢，结束游戏
            如打平，继续游戏
        输出结果
        """
        print("Welcome to Game!")
        print(self.List)
        
                
                
A_Game = RockPaperScissors()
A_Game.Game()
        
               
           
            
        
    