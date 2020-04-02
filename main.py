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
import Animat
import Animation
import spriteLib

#redimmensionne l'ecran
sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=35, cols=44))

#interaction clavier
old_settings = termios.tcgetattr(sys.stdin)

#donnee du jeu
animat=None
background = None
timeStep=None
animation=None


def init():
	global animat, background, timeStep, animation, film_animation, sprites

	#initialisation de la partie

	timeStep=0.1

	# creation des elements du jeu
	background = Background.create("image.txt")
	sprites = spriteLib.initSprites("sprite.txt")

	animat = Animat.create(color=3,
				direction="right",
				x=5.0,
				y=5.0,
				speed=6.0,
				sprite=sprites["little_ship"])


	#animation
	animation=Animation.create(color=4,x=28,y=8,filename="anim.txt")
	film_animation=Animation.create(color=4,x=24,y=0,filename="film.txt")

	# interaction clavier
	tty.setcbreak(sys.stdin.fileno())

	#effacer la console
	sys.stdout.write("\033[1;1H")
	sys.stdout.write("\033[2J")


def move():
	global animat, timeStep, animation
	#deplacement Animat
	x,y=Animat.computeNextPosition(timeStep,animat)

	if(Background.getChar(background,int(x),int(y))=='A'):
		#depart animation
		Animation.setOn(animation)
		Background.setChar(background,int(x),int(y),' ')

	if(Background.getChar(background,int(x),int(y))==' '):
		Animat.setPosition(animat,x,y)
	else:
		Background.setChar(background,int(x),int(y),'*')

def interact():
	global animat, background, timeStep, film, film_animation, sprites
	#gestion des evenement clavier

	#si une touche est appuyee
	if isData():
		c = sys.stdin.read(1)
		if c == '\x1b':         # x1b is ESC
			quitGame()
		elif c=='c' :
			Animat.changeColor(animat)
		elif c=='z' :
			Animat.changeDirection(animat,"z")
		elif c=='q' :
			Animat.changeDirection(animat,"q")
		elif c=='s' :
			Animat.changeDirection(animat,"s")
		elif c=='d' :
			Animat.changeDirection(animat,"d")
		elif c=='n' :
			Animat.randomPos(animat)
		elif c=='f':
			Animation.setOn(film_animation)
		elif c=='v':
			Animat.randomSprite(animat,sprites)

def isData():
	#recuperation evenement clavier
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def show():
	global background, animat, animation, timeStep

	#rafraichissement de l'affichage

	#effacer la console
	# sys.stdout.write("\033[1;1H")
	# sys.stdout.write("\033[2J")


	#affichage des different element

	Background.show(background)
	Animat.show(animat)

	Animation.show(animation,timeStep)
	Animation.show(film_animation,timeStep)

	#restoration couleur
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")

	#deplacement curseur
	sys.stdout.write("\033[1;1H\n")


def run():
	global timeStep

	#Boucle de simulation
	while 1:
		interact()
		move()
		show()
		time.sleep(timeStep)

def quitGame():

	#restoration parametres terminal
	global old_settings

	#couleur white
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")

	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
	sys.exit()

######################################

init()
#try:
run()
#finally:
quitGame()
