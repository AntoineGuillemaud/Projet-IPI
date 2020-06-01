import sys

def init():
	obstacle_list=list()
	return obstacle_list

def clear(obstacle_list):
	obstacle_list.clear()


def addObstacle(obstacle_list,pos_x,pos_y,sprite,color):

	obstacle=dict()
	obstacle["pos_x"]=pos_x
	obstacle["pos_y"]=pos_y
	obstacle["sprite"]=sprite
	obstacle["hitbox"]=computeHitbox(obstacle)
	obstacle["alive"]=True
	obstacle["color"]=6

	obstacle_list.append(obstacle)


def computeHitbox(obstacle):
    sprite = obstacle["sprite"]
    max_y = len(sprite)

    list_x = []
    for line in sprite:
        list_x.append(len(line))

    max_x = max(list_x)
    hitbox = (max_x,max_y)
    return hitbox


def show(obstacle_list,scrollLine):
    for obstacle in obstacle_list:
        if obstacle["alive"]==True:
            x=int(obstacle["pos_x"])
            y=int(obstacle["pos_y"])

            i=2
            print_y = scrollLine - y
            #couleur fond noire
            sys.stdout.write("\033[40m")

            #couleur player
            color=obstacle["color"]
            txt="\033[3"+str(color%7+1)+"m"
            sys.stdout.write(txt)

            #affichage du player
            sprite = obstacle["sprite"]

            for sprite_line in sprite:
                txt="\033["+str(int(print_y+i))+";"+str(x)+"H"
                sys.stdout.write(txt)

                sys.stdout.write(sprite_line)
                i=i+1

def killOutOfScreen(obstacle_list,scrollLine):
    for obstacle in obstacle_list:
        y=int(obstacle["pos_y"])
        print_y = scrollLine - y
        max_y = obstacle["hitbox"][1]
        if print_y >= (34 - max_y):
            obstacle["alive"] = False
