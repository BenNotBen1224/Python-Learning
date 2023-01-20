import random
import keyboard
import time

class RockPaperScissors:
    
    def __init__(self):
        
        self.List = ["Rock", "Paper", "Scissor"]
    
    def Check_Who_Wins(self):
        
        if(self.List.index(self.A) > self.List.index(self.B)):
            print("Player 1 Wins!")
        if(self.List.index(self.B) > self.List.index(self.A)):
            print("Player 2 Wins!")  
        else: 
            print("Draw, play again.")
    
    def Speed_Up_Mode(self):
        
        t = 5
        timer = "{:02d}:{:02d}".format(0, t)
        print(timer + "\r")
        time.sleep(1)
        t = t - 1
        
    def Game(self):
        """
        随机挑选玩家
        提示并记录玩家输入
        X Vs. Y
        判断输赢
            如输、赢，结束游戏
            如打平，继续游戏 
        """
        print("Welcome to Game!")
        
        while True: 
             
            print("Press Space If You Want to Speed Up the Game :)")
            #self.Speed_Up_Mode() if keyboard.wait('space') == True else print("Speed-Up Mode Disabled")
            
            if keyboard.wait('space') == False :
                self.Speed_Up_Mode() 
                print("Speed-Up Mode Enabled") 
            else:
                print("Speed-Up Mode Disabled")
            
            
        #记录玩家输入
            player1 = 'X' if random.randint(0, 1) == 0 else 'Y'
            self.A = self.List[int(input(f"{player1}'s turn (1. Rock 2. Paper 3. Scissor):")) - 1]
            
            for i in range (4):
                print("\n -")
            
            player2 = 'X' if player1 == 'Y' else 'Y'
            self.B = self.List[int(input(f"{player2}'s turn (1. Rock 2. Paper 3. Scissor):")) - 1]
            
            #显示玩家输入
            print(self.A + " Vs." + self.B)
            #判断输赢并输出结果
            self.Check_Who_Wins()
            #if keyboard.is_pressed(' '):
                
                
A_Game = RockPaperScissors()
A_Game.Game()
        
               
           
            
        
    