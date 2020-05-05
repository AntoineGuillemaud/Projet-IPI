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
    enemy["pos_y"] = pos_y
    enemy["sprite"] = sprite
    enemy["color"] = color
    enemy["hitbox"] = computeHitbox(enemy)
    enemy["behavior"] = behavior
    enemy["weapon"] = weapon
    enemy["on_screen"] = True
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


def show(enemyList,scrollLine):
    for enemy in enemyList:
        if enemy["on_screen"]==True:
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
            enemy["on_screen"] = False
