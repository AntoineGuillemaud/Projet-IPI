import sys
import os
import random
import Animation
import ammoLib
import hudLib

def create(color,direction,x,y,speed,sprite):

    player=dict()
    player["color"]=color
    player["HP"]=5
    player["direction"]=direction
    player["x"]=x
    player["y"]=y
    player["speed"]=speed
    player["sprite"]=sprite
    player["hitbox"]=computeHitbox(player)
    player["shooting"]=False
    player["cooldown"]=0

    return player

def switchShootingState(player):
    player["shooting"]= not player["shooting"]

def show(player) :

    x=int(player["x"])
    y=int(player["y"])

    #couleur fond noire
    sys.stdout.write("\033[40m")

    #couleur player
    c=player["color"]
    txt="\033[3"+str(c%7+1)+"m"
    sys.stdout.write(txt)

    #affichage du player
    sprite = player["sprite"]

    for sprite_line in sprite:
        txt="\033["+str(y)+";"+str(x)+"H"
        sys.stdout.write(txt)

        sys.stdout.write(sprite_line)
        y=y+1

def setSomeThing(player,key,value):
    player[key]=value
    return

def computeHitbox(player):
    sprite = player["sprite"]
    max_y = len(sprite)

    list_x = []
    for line in sprite:
        list_x.append(len(line))

    max_x = max(list_x)
    hitbox = (max_x,max_y)
    return hitbox

def ComputeAndApplyHitbox(player):
    hitbox=computeHitbox(player)
    setSomeThing(player,"hitbox",hitbox)
    return

def computeNextPosition(timeStep,player):
    #calcul de la position future du player en fonction du pas de temps
    screen_size_x = 44
    screen_size_y = 35

    hitbox_x , hitbox_y = player["hitbox"]

    x=player["x"]
    y=player["y"]
    if player["direction"]=="up" and y>3:
        y=(player["y"]-(player["speed"]*timeStep))
    elif player["direction"]=="right" and x+hitbox_x<screen_size_x:
        x=(player["x"]+(2*player["speed"]*timeStep))
    elif player["direction"]=="down" and y+hitbox_y<screen_size_y:
        y=(player["y"]+(player["speed"]*timeStep))
    elif player["direction"]=="left" and x > 3:
        x=(player["x"]-(2*player["speed"]*timeStep))
    return x,y

def setPosition(player,x,y):
    player["x"]=x
    player["y"]=y

def changeColor(player):
    player["color"]=player["color"]+1

def changeDirection(player,direction):
    if direction=="d":
        player["direction"]="right"
    elif direction=="s":
        player["direction"]="down"
    elif direction=="q":
        player["direction"]="left"
    elif direction=="z":
        player["direction"]="up"
    elif direction=="n":
        player["direction"]="null"

def randomPos(player):
    x_pos = random.randint(0,20)
    y_pos = random.randint(0,20)
    setPosition(player,x_pos,y_pos)

def changeSprite(player,sprite):
    player["sprite"]=sprite
    player["hitbox"]=computeHitbox(player)

def updateShooting(player,list_ammo,scrollLine):
    cooldown_rate = 0.8

    if (player["cooldown"] == 0.0) and (player["shooting"]):
        shoot(player,list_ammo,int(scrollLine))
        player["cooldown"]=10
    else:
        player["cooldown"] = max(0,player["cooldown"]-cooldown_rate)


def shoot(player,list_ammo,scrollLine):
    (relativ_pos_x,relativ_pos_y) = player["hitbox"]
    pos_x = player["x"] + relativ_pos_x/2
    pos_y = scrollLine - player["y"]+1

    side = 1
    color = 7

    ammoLib.appendAmmo(list_ammo,"small_laser",pos_x,pos_y,side,color)


def randomSprite(player,sprites):
    sprite_name = random.choice(list(sprites.keys()))
    changeSprite(player,sprites[sprite_name])
