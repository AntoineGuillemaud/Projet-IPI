import sys
import enemyLib

def create():

    list_ammo = list()

    return list_ammo

def clear(list_ammo):
    list_ammo.clear()

def appendAmmo(list_ammo,type,pos_x,pos_y,speed,side,color,carac1=None,carac2=None):

    ammo = dict()
    ammo["type"]=type
    ammo["pos_x"] = pos_x
    ammo["last_pos_y"] = pos_y
    ammo["pos_y"] = pos_y #la position dans le level, pas la position sur l'ecran
    ammo["speed"] = speed
    ammo["side"] = side
    ammo["color"] = color
    ammo["carac1"] = carac1
    ammo["carac2"] = carac2
    ammo["dammagePoint"]=1
    ammo["on_screen"] = True

    list_ammo.append(ammo)
    return

def move(list_ammo):
    for ammo in list_ammo:
        if (ammo["type"] == "plomb") and (ammo["on_screen"]==True):
            ammo["pos_y"] = ammo["pos_y"] + 1 * ammo["side"] * ammo["speed"]
    return

def killOutOfScreen(list_ammo,scrollLine):
    for ammo in list_ammo:
        y=int(ammo["pos_y"])
        print_y = scrollLine - y
        if y> scrollLine:
            ammo["on_screen"] = False

def impact(list_ammo,enemyList):
        for ammo in list_ammo:
            if ammo["on_screen"]:
                for enemy in enemyList:
                    if enemy["alive"]:
                        if isImpact(ammo,enemy):
                            enemyLib.takeDammage(enemy,ammo["dammagePoint"])
                            ammo["on_screen"]=False

def isImpact(ammo,enemy):
    ammo_pos_x = ammo["pos_x"]
    ammo_last_pos_y = ammo["last_pos_y"]
    ammo_pos_y = ammo["pos_y"]

    enemy_pos_x = enemy["pos_x"]
    enemy_pos_y = enemy["pos_y"]
    enemy_hitbox = enemy["hitbox"]
    enemy_hitbox_x,enemy_hitbox_y=enemy_hitbox

    if (ammo_pos_x>=enemy_pos_x) and (ammo_pos_x<enemy_pos_x+enemy_hitbox_x):

        ammo_inside =(ammo_pos_y<enemy_pos_y) and (ammo_pos_y >enemy_pos_y-enemy_hitbox_y)
        ammo_passed_trought = (ammo_last_pos_y < enemy_pos_y-enemy_hitbox_y) and (ammo_pos_y>enemy_pos_y)

        if (ammo_inside or ammo_passed_trought):
            return True
    return False



def show(list_ammo,scrollLine):
    for ammo in list_ammo:
        if ammo["on_screen"]:
            if ammo["type"] == "plomb":
                sprite = ["*"]

            x=int(ammo["pos_x"])
            y=int(scrollLine) - int(ammo["pos_y"])

            #couleur fond noire
            sys.stdout.write("\033[40m")

            #couleur ammo
            color = ammo["color"]
            txt="\033[3"+str(color%7+1)+"m"
            sys.stdout.write(txt)

            for sprite_line in sprite:
                txt="\033["+str(y)+";"+str(x)+"H"
                sys.stdout.write(txt)

                sys.stdout.write(sprite_line)
                y=y+1
