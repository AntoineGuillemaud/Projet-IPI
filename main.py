################
# main.c       #
# G.Desmeulles #
# 23/04/2013   #
# S2-P MDD     #
################

#modules externes
import sys
import os
import time
import select
import tty
import termios

#mes modules
import Background
import PlayerLib
import Animation
import spriteLib
import hudLib
import ammoLib
import chargeLevel
import enemySummonLib
import levelLib
import enemyLib
import enemyDBLib





#donnee du jeu
player=None
background = None
timeStep=None
animation=None
hud =None
level = None
level_length = None
list_ammo = None
level_list = None
enemySummonList = None
scrollLine = None
enemyDBList = None

def init():
    global player, background, timeStep, animation, film_animation, sprites, hud, level, list_ammo, level_list, enemySummonList, scrollLine, enemyDBList

    #initialisation de la partie

    timeStep=0.1

    # creation des elements du jeu
    background = Background.create("resources/image.txt")
    sprites = spriteLib.initSprites("resources/sprite.txt")
    hud = hudLib.initHUD()
    hudLib.initHUD_Game(hud)

    player = PlayerLib.create(color=3,
                direction="null",
                x=5.0,
                y=5.0,
                speed=6.0,
                sprite=sprites["little_ship"])


    #animation
    animation=Animation.create(color=4,x=28,y=8,filename="resources/anim.txt")
    film_animation=Animation.create(color=4,x=24,y=0,filename="resources/film.txt")

    level = 1

    scrollLine = 33

    enemyList = enemyLib.initEnemyList()

    list_ammo = ammoLib.create()

    level_list = chargeLevel.ChargeLevelIntoRAM(sprites)

    enemyDBList = enemyDBLib.init(sprites)

    enemySummonList = enemySummonLib.init()

    levelLib.changeLevel(level,player,hud,level_list,enemySummonList,enemyList,list_ammo,scrollLine)



def move():
    global player, timeStep, animation
    #deplacement Animat
    x,y=PlayerLib.computeNextPosition(timeStep,player)
    PlayerLib.setPosition(player,x,y)


def interact():
    global player, background, timeStep, film, film_animation, sprites
    #gestion des evenement clavier

    #si une touche est appuyee
    if isData():
        c = sys.stdin.read(1)
        termios.tcflush(sys.stdin,termios.TCIFLUSH)
        if c == '\x1b':         # x1b is ESC
            quitGame()
        elif c=='c' :
            PlayerLib.changeColor(player)
        elif c=='z' :
            PlayerLib.changeDirection(player,"z")
        elif c=='q' :
            PlayerLib.changeDirection(player,"q")
        elif c=='s' :
            PlayerLib.changeDirection(player,"s")
        elif c=='d' :
            PlayerLib.changeDirection(player,"d")
        elif c=='n' :
            PlayerLib.randomPos(player)
        elif c=='f':
            Animation.setOn(film_animation)
        elif c=='v':
            PlayerLib.randomSprite(player,sprites)
    else:
        PlayerLib.changeDirection(player,"n")


def isData():
    #recuperation evenement clavier
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def show():
    global background, player, animation, timeStep, hud

    #rafraichissement de l'affichage

    #effacer la console
    # sys.stdout.write("\033[1;1H")
    # sys.stdout.write("\033[2J")


    #affichage des different element

    Background.show(background)
    PlayerLib.show(player)

    Animation.show(animation,timeStep)
    Animation.show(film_animation,timeStep)
    hudLib.showHUD(hud)

    #restoration couleur
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")

    #deplacement curseur
    sys.stdout.write("\033[1;1H\n")


def run():
    global timeStep

    #Boucle de simulation
    while 1:
        time_start = time.time()
        interact()
        move()
        show()
        time_end = time.time()
        time.sleep(max(0,timeStep - (time_end-time_start)))

def quitGame():

    #restoration parametres terminal
    global old_settings

    #couleur white
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    sys.exit()

######################################
