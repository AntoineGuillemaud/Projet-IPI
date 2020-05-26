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
import scrollBackgroundLib





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
enemy_types = None
enemy_behaviors = None
lastScrollTime = None
scrollBackgroundList = None
scrollBackground = None
list_type_ammo=None

def init():
    global player, background, timeStep, level_length,list_type_ammo, animation,scrollBackgroundList,enemy_behaviors, scrollBackground, film_animation, enemyList, sprites, hud, level, list_ammo, level_list, enemySummonList,scrollSpeed, scrollLine, enemy_types, lastScrollTime

    #initialisation de la partie

    timeStep=0.1

    # creation des elements du jeu
    background = Background.create("resources/bordure.txt")

    scrollBackgroundList = scrollBackgroundLib.init("resources/scrollBackground_file.txt")


    sprites = spriteLib.initSprites("resources/sprite.txt")

    hud = hudLib.initHUD()
    hudLib.initHUD_Game(hud)

    player = PlayerLib.create(color=3,
                direction="null",
                x=20.0,
                y=28.0,
                speed=6.0,
                sprite=sprites["little_ship"])



    level = 1

    lastScrollTime = time.time()

    scrollLine = 33
    scrollSpeed = 10

    enemyList = enemyLib.initEnemyList()

    list_ammo = ammoLib.create()

    list_type_ammo = ammoLib.initAmmoDB()

    scrollBackground = scrollBackgroundList["level1"]

    enemy_types, enemy_behaviors = enemyDBLib.init(sprites)

    enemySummonList = enemySummonLib.init()

    level_list = chargeLevel.ChargeLevelIntoRAM(sprites,scrollBackgroundList,enemy_behaviors)

    level_length = levelLib.changeLevel(level,player,hud,level_list,enemySummonList,enemyList,list_ammo,scrollLine,scrollBackground,scrollBackgroundList)


def interact():
    global player, background, timeStep, film, film_animation, sprites, hud
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
        elif c=='v':
            PlayerLib.randomSprite(player,sprites)
        elif c=='r':
            PlayerLib.switchShootingState(player)


    else:
        PlayerLib.changeDirection(player,"n")


def isData():
    #recuperation evenement clavier
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def show():
    global background, player, animation, timeStep, hud,enemyList,level_length,scrollBackground, scrollLine,list_type_ammo

    Background.show(background)
    scrollBackgroundLib.show(scrollBackground,level_length,scrollLine)
    ammoLib.show(list_ammo,scrollLine,list_type_ammo)
    enemyLib.show(enemyList,scrollLine)
    PlayerLib.show(player)

    hudLib.HUDChangeSomething(hud,"vies","value",player["HP"])
    hudLib.HUDChangeSomething(hud,"special1","value",scrollLine)
    hudLib.showHUD(hud)

    #restoration couleur
    sys.stdout.write("\033[37m")
    sys.stdout.write("\033[40m")

    #deplacement curseur
    sys.stdout.write("\033[1;1H\n")

def updateScroll():
    global scrollLine, lastScrollTime, timeStep, hud, scrollSpeed,player

    beforeLastScrollTime = lastScrollTime

    lastScrollTime = time.time()

    scrollLine = scrollLine + (lastScrollTime - beforeLastScrollTime) * scrollSpeed * timeStep

    hudLib.HUDChangeSomething(hud,"ammo","value",player["y"])
    hudLib.HUDChangeSomething(hud,"special1","value",scrollLine)


def move():
    global player, timeStep, animation, enemyList,scrollLine,hud,list_type_ammo
    #deplacement Animat
    x,y=PlayerLib.computeNextPosition(timeStep,player)
    PlayerLib.setPosition(player,x,y)
    enemyLib.move(enemyList,scrollLine)
    ammoLib.move(list_ammo,list_type_ammo)


def live():
    global enemySummonList,enemyList,scrollLine, enemy_types,player,list_ammo,list_type_ammo

    updateScroll()
    move()
    PlayerLib.updateShooting(player,list_ammo,scrollLine)
    enemySummonLib.summonEnemy(enemySummonList,enemyList,scrollLine,enemy_types)
    enemyLib.killOutOfScreen(enemyList,scrollLine)
    enemyLib.updateShooting(enemyList,list_ammo,scrollLine)
    ammoLib.killOutOfScreen(list_ammo,scrollLine)
    ammoLib.impact(list_ammo,enemyList,list_type_ammo,player,scrollLine)

def run():
    global timeStep

    #Boucle de simulation
    while 1:
        time_start = time.time()
        interact()
        live()
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
