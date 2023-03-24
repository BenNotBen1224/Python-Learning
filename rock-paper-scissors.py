import random
import keyboard
import time
import threading

class RockPaperScissors:
    
    #建立选择库
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
            
            t = 0
            #显示剩余时间
            if(stop == False):
                t = sec
                timer = "{:02d}:{:02d}".format(0, t)
                print("\r" + timer, end =  "\r")
                time.sleep(1)
                t = t - 1
                
            #查看是否继续
            if(t > 0):
                Speed_Up_Mode(sec - 1)
            elif t == 0:
                t = 0 
            else: 
                print("\r" + "       ", end =  "\r")
                print("\n" + "Null, Game Ended")
        
 
        print("Welcome to Game! \n") 
        print("Press Space If You Want to Speed Up the Game, else pressed any other button")
              
        if keyboard.read_key() == 'space':
            print("Speed-Up Mode Enabled")
            #建立子线程
            thread1 = threading.Thread(target = Speed_Up_Mode, name = "Speed-Up-Mode", args=(5,))
            thread1.start()
                 
        else:
            print("Speed-Up Mode Disabled")
            
            
        #记录玩家输入　
        player1 = 'X' if random.randint(0, 1) == 0 else 'Y'
        self.A = self.List[int(input("       " + f"{player1}'s turn (1. Rock 2. Paper 3. Scissor)       :")) - 1]
        
        stop = True
         
        for i in range (4):
            print("\n -")
        
        stop = False
        thread2 = threading.Thread(target = Speed_Up_Mode, name = "Speed-Up-Mode", args=(5,))
        thread2.start()
        
        player2 = 'X' if player1 == 'Y' else 'Y'
        self.B = self.List[int(input("        " + f"{player2}'s turn (1. Rock 2. Paper 3. Scissor):")) - 1]
        
        stop = True
        
        #显示玩家输入
        print(self.A + " Vs." + self.B)
        #判断输赢并输出结果
        self.Check_Who_Wins()
                         
A_Game = RockPaperScissors()
A_Game.Game()
        
               
           
            
        
    