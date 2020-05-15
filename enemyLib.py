################
# sprite.py    #
# A.Guillemaud #
# 05/04/2020   #
# S2-P IPI     #
################

import sys
import hudLib

def initEnemyList():
    enemyList = list()
    return enemyList

def clearEnemyList(enemyList):
    enemyList = list()

def initEnemy(enemyList,HP,pos_x,pos_y,sprite,color,behavior,weapon):
    enemy = dict()
    enemy["HP"] = HP
    enemy["pos_x"] = pos_x
    enemy["pos_y"] = pos_y #la position dans le level, pas la position sur l'ecran
    enemy["sprite"] = sprite
    enemy["color"] = color
    enemy["hitbox"] = computeHitbox(enemy)
    enemy["behavior"] = behavior
    enemy["weapon"] = weapon
    enemy["alive"] = True
    enemyList.append(enemy)


def computeHitbox(enemy):
    sprite = enemy["sprite"]
    max_y = len(sprite)

    list_x = []
    for line in sprite:
        list_x.append(len(line))

    max_x = max(list_x)
    hitbox = (max_x,max_y)
    return hitbox

def takeDammage(enemy,dammagePoint):
    enemy["HP"] = max(0,enemy["HP"]-dammagePoint)

    if enemy["HP"] == 0:
        kill(enemy)

def move(enemyList):
    for enemy in enemyList:
        enemy["behavior"](enemy)

def move_direction(enemy,direction,step):
    if direction == -1:
        enemy["pos_x"]=max(2,enemy["pos_x"] + direction*step)
    elif direction == 1:
        hx,hy =enemy["hitbox"]
        enemy["pos_x"]=min(44-hx,enemy["pos_x"] + direction*step)

def show(enemyList,scrollLine):
    for enemy in enemyList:
        if enemy["alive"]==True:
            x=int(enemy["pos_x"])
            y=int(enemy["pos_y"])

            i=2
            print_y = scrollLine - y
            #couleur fond noire
            sys.stdout.write("\033[40m")

            #couleur player
            color=enemy["color"]
            txt="\033[3"+str(color%7+1)+"m"
            sys.stdout.write(txt)

            #affichage du player
            sprite = enemy["sprite"]

            for sprite_line in sprite:
                txt="\033["+str(int(print_y+i))+";"+str(x)+"H"
                sys.stdout.write(txt)

                sys.stdout.write(sprite_line)
                i=i+1

def killOutOfScreen(enemyList,scrollLine):
    for enemy in enemyList:
        y=int(enemy["pos_y"])
        print_y = scrollLine - y
        max_x , max_y = enemy["hitbox"]
        if print_y >= (35 - max_y):
            enemy["alive"] = False

def kill(enemy):
    enemy["alive"]=False
