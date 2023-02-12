import pyautogui
import time
import keyboard
import random
import sys
import win32api, win32con
import tkinter
from threading import Thread

busquedas = ["amazon.com","pinterest.com",
"reddit.com","facebook.com",
"elcorteingles.com","twitch.tv",
"ikea.com","google.com",
"quora.com","wikipedia.com",
"youtube.com","tappedout.net",
"https://warthunder.com/","https://www.lamoncloa.gob.es/Paginas/index.aspx",
"steamcommunity.com","www.epicgames.com",
"","milanuncios.com",
"yahoo.com", "https://www.minecraft.net",
"https://www.decathlon.es/","https://stackoverflow.com/",
"https://www.bitstamp.net/","",
"twitter.com","spotify.com",
"https://www.d20pfsrd.com/alternative-rule-systems/occult-adventures/occult-classes/mesmerist/","",
"https://www.d20pfsrd.com/classes/core-classes/cleric/","https://www.d20pfsrd.com/classes/core-classes/fighter/",
"google.com","google.com",
"","",
"","",
"","",
"","",
]

#The bot works properly if Brave is in a fullscreen view.
screen1 = tkinter.Tk()
screenWidth = screen1.winfo_screenwidth()
screenHeight = screen1.winfo_screenheight()

print(screenWidth)
print(screenHeight)

def main():
    global stop_thread
    stop_thread = False
    Bot().start()
    while keyboard.is_pressed('p') == False:
        sys.stdout.write('main is active \r')
    print('Input to pause listened')
    stop_thread = True
    print('Chester stopped')



class Bot(Thread):

    def run(self):
        print('Chester is running')
        Bot.search(self)

    def sleep(sleepTime):
        time.sleep(sleepTime)

    def rngSleep(self):
        print("rngsleep")
        chanceOfSleep = random.randint(0,7)
        rngTimeSleep = random.randint(30,120)
        print(chanceOfSleep)
        if chanceOfSleep > 0:
            time.sleep(rngTimeSleep)
            print("Sleeping")
        exit()


    def click(x,y):
        pyautogui.moveTo(x, y, duration=2, tween=pyautogui.easeInOutQuad)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    def search(self):
        if stop_thread == False:
            n = random.randint(1,3)
            rng = random.randint(0,len(busquedas))
            Bot.click(800,46)
            print('clickado')
            keyboard.send("backspace")
            pyautogui.write(busquedas[rng], interval=0.2)
            keyboard.send("enter")
            time.sleep(n)
            Bot.move(self)

    def restart(self):
        if stop_thread == False:
            Bot.click(22,47)
            print('clickado, Backwards')
            Bot.search(self)
        

    def move(self):
        if stop_thread == False:    
            rngcount = random.randint(0,5)
            countable = 0
            print("rngmove before while")
            while rngcount > countable | stop_thread == False: 
                print("rngmove inside while")
                rngmovex = random.randint(300,screenWidth - 500)
                rngmovey = random.randint(200,screenHeight - 200)
                chanceofclick1 = random.randint(0,1)
                chanceofclick2 = random.randint(0,1)
                rngduration = random.randint(3,6)
                print("rng premovimiento")
                pyautogui.moveTo(rngmovex,rngmovey, duration=rngduration, tween=pyautogui.easeInOutQuad)
                if(chanceofclick1 == chanceofclick2):
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                countable = countable + 1
            Bot.restart(self)
#Start
main()
