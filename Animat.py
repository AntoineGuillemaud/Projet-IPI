################
# Animat.py    #
# G.Desmeulles #
# 23/04/2013   #
# S2-P MDD     #
################
import sys
import os
import random
import Animation

#le module animat gere le type abstrait de donnee animat
#un animat est un objet qui se deplace dans le terminal

def create(color,direction,x,y,speed,sprite):

	#creation animat
	animat=dict()
	animat["color"]=color
	animat["direction"]=direction
	animat["x"]=x
	animat["y"]=y
	animat["speed"]=speed
	animat["sprite"]=sprite
	animat["hitbox"]=computeHitbox(animat)

	return animat

def show(a) :

	x=int(a["x"])
	y=int(a["y"])

	#couleur fond noire
	sys.stdout.write("\033[40m")

	#couleur animat
	c=a["color"]
	txt="\033[3"+str(c%7+1)+"m"
	sys.stdout.write(txt)

	#affichage de l animat
	sprite = a["sprite"]

	for sprite_line in sprite:
		txt="\033["+str(y)+";"+str(x)+"H"
		sys.stdout.write(txt)

		sys.stdout.write(sprite_line)
		y=y+1


def computeHitbox(a):
	sprite = a["sprite"]
	max_y = len(sprite)

	list_x = []
	for line in sprite:
		list_x.append(len(line))

	max_x = max(list_x)
	hitbox = (max_x,max_y)
	return hitbox


def computeNextPosition(dt,a):
	#calcul de la position future de l animat en fonction du pas de temps
	screen_size_x = 44
	screen_size_y = 35

	hitbox_x , hitbox_y = a["hitbox"]

	x=a["x"]
	y=a["y"]
	if a["direction"]=="up" and y>3:
		y=(a["y"]-(a["speed"]*dt))
	elif a["direction"]=="right" and x+hitbox_x<screen_size_x:
		x=(a["x"]+(2*a["speed"]*dt))
	elif a["direction"]=="down" and y+hitbox_y<screen_size_y:
		y=(a["y"]+(a["speed"]*dt))
	elif a["direction"]=="left" and x > 3:
		x=(a["x"]-(2*a["speed"]*dt))
	return x,y

def setPosition(a,x,y):
	a["x"]=x
	a["y"]=y

def changeColor(a):
	a["color"]=a["color"]+1

def changeDirection(a,direction):
	if direction=="d":
		a["direction"]="right"
	elif direction=="s":
		a["direction"]="down"
	elif direction=="q":
		a["direction"]="left"
	elif direction=="z":
		a["direction"]="up"
	elif direction=="n":
		a["direction"]="null"

def randomPos(a):
	x_pos = random.randint(0,20)
	y_pos = random.randint(0,20)
	setPosition(a,x_pos,y_pos)

def changeSprite(a,sprite):
	a["sprite"]=sprite
	a["hitbox"]=computeHitbox(a)


def randomSprite(a,sprites):
	sprite_name = random.choice(list(sprites.keys()))
	changeSprite(a,sprites[sprite_name])
