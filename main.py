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
import spriteLib
import hudLib
import ammoLib
import chargeLevel
import enemySummonLib
import levelLib
import enemyLib
import enemyDBLib
import scrollBackgroundLib
import obstacleLib
import obstacleSummonLib
import colisionLib




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
obstacle_list=None
obstacleSummon_list=None

def init():
    global player, background, timeStep,obstacle_list,obstacleSummon_list, level_length,list_type_ammo, animation,scrollBackgroundList,enemy_behaviors, scrollBackground, film_animation, enemyList, sprites, hud, level, list_ammo, level_list, enemySummonList,scrollSpeed, scrollLine, enemy_types, lastScrollTime

    #initialisation de la partie

    timeStep=0.1

    # creation des elements du jeu
    background = Background.create("resources/bordure.txt")

    scrollBackgroundList = scrollBackgroundLib.init("resources/scrollBackground_file.txt")


    sprites = spriteLib.initSprites("resources/sprite.txt")

    hud = hudLib.initHUD()
    hudLib.initHUD_Game(hud)

    player = PlayerLib.create(color=1,
                direction="null",
                x=20.0,
                y=28.0,
                speed=6.0,
                sprite=sprites["little_ship"],
                ammo_quantity=99,
                ammo_type="small_laser",
                HP=10,
                capacity_1=None)


    level = 1

    lastScrollTime = time.time()

    scrollLine = 33
    scrollSpeed = 10

    enemyList = enemyLib.initEnemyList()

    list_ammo = ammoLib.create()

    list_type_ammo = ammoLib.initAmmoDB()

    scrollBackground = list(scrollBackgroundList["level1"])

    enemy_types, enemy_behaviors = enemyDBLib.init(sprites)

    enemySummonList = enemySummonLib.init()

    obstacle_list = obstacleLib.init()
    obstacleSummon_list = obstacleSummonLib.init()

    level_list = chargeLevel.ChargeLevelIntoRAM(sprites,scrollBackgroundList,enemy_behaviors)

    level_length , scrollLine = levelLib.changeLevel(level,player,hud,level_list,enemySummonList,enemyList,list_ammo,scrollLine,scrollBackground,scrollBackgroundList,obstacle_list,obstacleSummon_list)


def interact():
    global player, background, timeStep, film, film_animation, sprites, hud,scrollLine,level
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
        elif c=='r':
            PlayerLib.switchShootingState(player)



    else:
        PlayerLib.changeDirection(player,"n")


def isData():
    #recuperation evenement clavier
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def show():
    global background, player, animation, timeStep, hud,enemyList,level_length,scrollBackground, scrollLine,list_type_ammo,obstacle_list,level

    Background.show(background)
    scrollBackgroundLib.show(scrollBackground,level_length,scrollLine)
    ammoLib.show(list_ammo,scrollLine,list_type_ammo)
    obstacleLib.show(obstacle_list,scrollLine)
    enemyLib.show(enemyList,scrollLine)
    PlayerLib.show(player)

    hudLib.HUDChangeSomething(hud,"vies","value",player["HP"])
    hudLib.HUDChangeSomething(hud,"niveau","value",level)
    hudLib.HUDChangeSomething(hud,"ammo","value",player["ammo_quantity"])
    hudLib.HUDChangeSomething(hud,"score","value",player["score"])
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


def move():
    global player, timeStep, animation, enemyList,scrollLine,hud,list_type_ammo
    #deplacement Animat
    x,y=PlayerLib.computeNextPosition(timeStep,player)
    PlayerLib.setPosition(player,x,y)
    enemyLib.move(enemyList,scrollLine)
    ammoLib.move(list_ammo,list_type_ammo)


def live():
    global enemySummonList,enemyList,scrollLine, enemy_types,player,list_ammo,list_type_ammo,obstacle_list,obstacleSummon_list,level_length,lenght,hud,level_list,scrollBackground,scrollBackgroundList,level

    updateScroll()
    if player["HP"]<=0:
        level_length , scrollLine = levelLib.changeLevel(level,player,hud,level_list,enemySummonList,enemyList,list_ammo,scrollLine,scrollBackground,scrollBackgroundList,obstacle_list,obstacleSummon_list)
    if scrollLine+21>=level_length:
        #level=level+1   #malheureusement pas eu le temps pour d'autres niveaux
        #level_length , scrollLine = levelLib.changeLevel(level,player,hud,level_list,enemySummonList,enemyList,list_ammo,scrollLine,scrollBackground,scrollBackgroundList,obstacle_list,obstacleSummon_list)
        print("Le jeu est fini")
        quitGame()
    PlayerLib.updateColor(player)
    move()
    colisionLib.checkColision(player,enemyList,obstacle_list,scrollLine)
    PlayerLib.updateShooting(player,list_ammo,scrollLine)
    enemySummonLib.summonEnemy(enemySummonList,enemyList,scrollLine,enemy_types)
    obstacleSummonLib.summonObstacle(obstacleSummon_list,obstacle_list,scrollLine,level)
    enemyLib.updateShooting(enemyList,list_ammo,scrollLine)
    enemyLib.killOutOfScreen(enemyList,scrollLine)
    obstacleLib.killOutOfScreen(obstacle_list,scrollLine)
    ammoLib.killOutOfScreen(list_ammo,scrollLine,list_type_ammo)
    colisionLib.checkColision(player,enemyList,obstacle_list,scrollLine)
    ammoLib.impact(list_ammo,enemyList,list_type_ammo,player,scrollLine,obstacle_list)

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
