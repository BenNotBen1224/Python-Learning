import random
import keyboard
import time
import threading

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
    
   
    
    def Game(self):
        """
        随机挑选玩家
        提示并记录玩家输入
        X Vs. Y 
        判断输赢
            如输、赢，结束游戏
            如打平，继续游戏 
        """
        
        stop = False
        
        def Speed_Up_Mode(sec,):
            
            if(stop == False):
                t = sec
                timer = "{:02d}:{:02d}".format(0, t)
                print("\r" + timer )
                time.sleep(1)
                t = t - 1
        
            if(t > 0):
                Speed_Up_Mode(sec - 1) 
            else:
                print("Null, Game Ended")
                return False
        
        while True: 
            
            print("Welcome to Game! \n") 
            print("Press Space If You Want to Speed Up the Game :)")
             
            if keyboard.read_key() == 'space':
                print("Speed-Up Mode Enabled")
                player1 = 'X' if random.randint(0, 1) == 0 else 'Y'
                self.A = self.List[int(input(f"{player1}'s turn (1. Rock 2. Paper 3. Scissor):")) - 1] 
                #怎么让子线程检测到主线程进展？
                thread = threading.Thread(target = Speed_Up_Mode, name = "Speed-Up-Mode", args=(5,))
                thread.start()
                # if [self.A != self.List[i] for i in range (3)]:
                #     print("Null, Game Ended")
                #     return False
                 
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
        
               
           
            
        
    