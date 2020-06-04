import time
import Background
import sys
import hudLib
import select
import termios
import tty
import cinematic


introCinematic=None
startMenuBackground=None
startMenuHelp=None
timeStep=None
hud=None
curseur =1
showHelp=True

def init():
    global startMenuBackground , timeStep, hud,showHelp,startMenuHelp,introCinematic
    startMenuBackground = Background.create("resources/startMenuBackground.txt")
    startMenuHelp = Background.create("resources/startMenuHelp.txt")
    introCinematic = cinematic.create("resources/cinematic.txt")

    timeStep=0.1

    hud = hudLib.initHUD()
    hudLib.initHUD_StartMenu(hud)


    cinematic.showEntireCinematic(introCinematic)

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
    global startMenuBackground, hud,showHelp

    if showHelp==False:
        Background.show(startMenuBackground)
        hudLib.showHUD(hud)
    if showHelp==True:
        Background.show(startMenuHelp)

    #restoration couleur
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")

    #deplacement curseur
    sys.stdout.write("\033[1;1H\n")


def interact(old_settings):
    global showHelp
    isStartMenuActive = True
    #si une touche est appuyee
    if isData():
        c = sys.stdin.read(1)
        termios.tcflush(sys.stdin,termios.TCIFLUSH)
        if c == '\x1b':         # x1b is ESC
            quitGame(old_settings)
        elif c=='z' and not showHelp :
            curseurMove("up")
        elif c=='s' and not showHelp:
            curseurMove("down")
        elif c=='\n' and not showHelp:
            isStartMenuActive = enterPressed(old_settings)
        elif c=='\n' and showHelp:
            showHelp=False
    return isStartMenuActive


def curseurMove(move_direction):
    global curseur
    if move_direction =="up" and curseur >0:
        curseur -= 1
    if move_direction =="down" and curseur <3:
        curseur += 1

def curseurChangeColor():
    global curseur, hud
    codex = {0:"continuer",1:"nouvelle",2:"comment_jouer",3:"quitter"}

    hudLib.HUDChangeColor(hud,codex[0],1)
    hudLib.HUDChangeColor(hud,codex[1],1)
    hudLib.HUDChangeColor(hud,codex[2],1)
    hudLib.HUDChangeColor(hud,codex[3],1)

    hudLib.HUDChangeColor(hud,codex[curseur],6)
    return

def enterPressed(old_settings):
    global curseur,showHelp
    if curseur   ==0:
        return True
    elif curseur ==1:
        return False
    elif curseur ==2:
        showHelp = True
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
