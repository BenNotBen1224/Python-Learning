import time

t = int(input("Please enter time in seconds:"))

def Timer(t):
    while t != 0:
        min, sec = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(min, sec)
        print(timer , end="\r")
        time.sleep(1)
        t = t - 1
    
print("Done")

Timer(t)