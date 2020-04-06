################
# sprite.py    #
# A.Guillemaud #
# 05/04/2020   #
# S2-P IPI     #
################

import sys

def initEnemy(HP,pos_x,sprite,color,behavior,weapon):
    enemy = dict()
    enemy["HP"] = HP
    enemy["pos_x"] = pos_x
    enemy["pos_y"] = 0
    enemy["sprite"] = sprite
    enemy["color"] = color
    enemy["hitbox"] = computeHitbox(enemy)
    enemy["behavior"] = behavior
    enemy["weapon"] = weapon
    return enemy


def computeHitbox(enemy):
	sprite = enemy["sprite"]
	max_y = len(sprite)

	list_x = []
	for line in sprite:
		list_x.append(len(line))

	max_x = max(list_x)
	hitbox = (max_x,max_y)
	return hitbox

def show(enemy) :

	x=int(enemy["pos_x"])
	y=int(enemy["pos_y"])

	#couleur fond noire
	sys.stdout.write("\033[40m")

	#couleur player
	color=enemy["color"]
	txt="\033[3"+str(color%7+1)+"m"
	sys.stdout.write(txt)

	#affichage du player
	sprite = enemy["sprite"]

	for sprite_line in sprite:
		txt="\033["+str(y)+";"+str(x)+"H"
		sys.stdout.write(txt)

		sys.stdout.write(sprite_line)
		y=y+1