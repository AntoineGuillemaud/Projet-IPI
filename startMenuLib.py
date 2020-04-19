import time
import Background
import sys
import hudLib
import select
import termios
import tty

startMenuBackground=None
timeStep=None
hud=None
curseur =1

def init():
    global startMenuBackground , timeStep, hud
    startMenuBackground = Background.create("resources/startMenuBackground.txt")

    timeStep=0.1

    hud = hudLib.initHUD()
    hudLib.initHUD_StartMenu(hud)


def close():
    return


def run(old_settings):
    global startMenuBackground, timeStep
    isStartMenuActive = True
    while 1:
        isStartMenuActive = interact(old_settings)
        if isStartMenuActive ==False:
            return False
        curseurChangeColor()
        show()
        time.sleep(timeStep)


def show():
    global startMenuBackground, hud

    Background.show(startMenuBackground)
    hudLib.showHUD(hud)

    #restoration couleur
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")

    #deplacement curseur
    sys.stdout.write("\033[1;1H\n")


def interact(old_settings):

    isStartMenuActive = True
    #si une touche est appuyee
    if isData():
        c = sys.stdin.read(1)
        termios.tcflush(sys.stdin,termios.TCIFLUSH)
        if c == '\x1b':         # x1b is ESC
            quitGame(old_settings)
        elif c=='z' :
            curseurMove("up")
        elif c=='s' :
            curseurMove("down")
        elif c=='\n' :
            isStartMenuActive = enterPressed(old_settings)
    return isStartMenuActive


def curseurMove(move_direction):
    global curseur
    if move_direction =="up" and curseur >0:
        curseur -= 1
    if move_direction =="down" and curseur <3:
        curseur += 1

def curseurChangeColor():
    global curseur, hud
    codex = {0:"continuer",1:"nouvelle",2:"charger",3:"quitter"}

    hudLib.HUDChangeColor(hud,codex[0],1)
    hudLib.HUDChangeColor(hud,codex[1],1)
    hudLib.HUDChangeColor(hud,codex[2],1)
    hudLib.HUDChangeColor(hud,codex[3],1)

    hudLib.HUDChangeColor(hud,codex[curseur],6)
    return

def enterPressed(old_settings):
    global curseur
    if curseur   ==0:
        return True
    elif curseur ==1:
        return False
    elif curseur ==2:
        return True
    elif curseur ==3:
        quitGame(old_settings)

    return True



def isData():
    #recuperation evenement clavier
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])



def quitGame(old_settings):


    #couleur white
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    sys.exit()
