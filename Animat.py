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






def computeNextPosition(dt,a):
	#calcul de la position future de l animat en fonction du pas de temps
	x=a["x"]
	y=a["y"]
	if a["direction"]=="up":
		y=(a["y"]-(a["speed"]*dt))
	elif a["direction"]=="right":
		x=(a["x"]+(2*a["speed"]*dt))
	elif a["direction"]=="down":
		y=(a["y"]+(a["speed"]*dt))
	elif a["direction"]=="left":
		x=(a["x"]-(2*a["speed"]*dt))
	elif a["direction"]=="null":
		x=x
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

def randomSprite(a,sprites):
	sprite_name = random.choice(list(sprites.keys()))
	changeSprite(a,sprites[sprite_name])
