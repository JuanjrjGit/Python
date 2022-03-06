import pyautogui
import time
import keyboard
import random
import win32api, win32con

#n = random.randint(0,2)
contador = 10
ciclo = 0
busquedas = ["amazon.com","pinterest.com",
"reddit.com","facebook.com",
"elcorteingles.com","twitch.tv",
"ikea.com","google.com",
"quora.com","wikipedia.com",
"youtube.com","tappedout.net",
"https://warthunder.com/","https://www.lamoncloa.gob.es/Paginas/index.aspx",
"steamcommunity.com","www.epicgames.com",
"https://azurlane.yo-star.com/#/","milanuncios.com",
"yahoo.com", "https://www.minecraft.net",
"https://www.decathlon.es/","https://stackoverflow.com/",
"https://www.bitstamp.net/","",
"twitter.com","spotify.com",
"https://www.d20pfsrd.com/alternative-rule-systems/occult-adventures/occult-classes/mesmerist/","",
"https://www.d20pfsrd.com/classes/core-classes/cleric/","https://www.d20pfsrd.com/classes/core-classes/fighter/",
"google.com","google.com",
"https://github.com/","https://about.gitlab.com/",
"https://es.wikipedia.org/wiki/Lua","https://es.wikipedia.org/wiki/Java_(lenguaje_de_programaci%C3%B3n)",
"","",
"","",
]
modo = 0 # Va a tener 3 modos, inicio 0, búsqueda 1, vuelta 2, que se va a llevar a lo largo de 15 segundos todos + numero random 
#El modo de inicio, escribe en el buscador y busca
def click1(x,y):
    #win32api.SetCursorPos((x,y))
    pyautogui.moveTo(x, y, duration=2, tween=pyautogui.easeInOutQuad)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def rngmove():
    try:
        print("rngmove starts")
        rngcount = random.randint(0,5)
        countable = 0
        print("rngmove before while")
        while rngcount > countable: 
            print("rngmove inside while")
            rngmovex = random.randint(100,800)
            rngmovey = random.randint(200,850)
            chanceofclick1 = random.randint(0,1)
            chanceofclick2 = random.randint(0,1)
            rngduration = random.randint(2,8)
            print("rng premovimiento")
            pyautogui.moveTo(rngmovex,rngmovey, duration=rngduration, tween=pyautogui.easeInBounce)
            if(chanceofclick1 == chanceofclick2):
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            countable = countable + 1
    except:
        print('Iteracion rng')
while keyboard.is_pressed('p') == False:
    try:
        n = random.randint(1,3)
        if modo == 2:
            click1(22,47)
            print('clickado, retroceso')
            time.sleep(1)
            modo = 0
        elif modo == 1:
            #click1(395,291)
            rngmove()
            print('clickado, vuelta')
            time.sleep(5)
            modo = 2
        elif modo == 0:
            rng = random.randint(0,len(busquedas))
            click1(800,46)
            print('clickado')
            keyboard.send("backspace")
            pyautogui.write(busquedas[rng], interval=0.4)
            keyboard.send("enter")
            print('buscando')
            print(rng) 
            print("dormido")
            time.sleep(n)
            modo = 1    
    except:
        #pyautogui.alert("Chester has been stopped")
        print('Iteracion fallida')
pyautogui.alert("Chester has been stopped")
print('Proceso parado')