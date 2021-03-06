import sys
import PlayerLib
import enemyLib

def create():

    list_ammo = list()

    return list_ammo

def clear(list_ammo):
    print(list_ammo)
    list_ammo.clear()

def appendAmmo(list_ammo,type,pos_x,pos_y,side,color,carac1=None,carac2=None):

    ammo = dict()
    ammo["type"]=type
    ammo["pos_x"] = pos_x
    ammo["last_pos_y"] = pos_y
    ammo["pos_y"] = pos_y #la position dans le level, pas la position sur l'ecran
    ammo["side"] = side
    ammo["color"] = color
    ammo["carac1"] = carac1
    ammo["carac2"] = carac2
    ammo["on_screen"] = True

    list_ammo.append(ammo)
    return

def move(list_ammo,list_type_ammo):
    for ammo in list_ammo:
        if ammo["on_screen"]:
            ammo["last_pos_y"] = ammo["pos_y"]
            ammo["pos_y"] = ammo["pos_y"] + 1 * ammo["side"] * list_type_ammo[ammo["type"]]["speed"]
    return

def killOutOfScreen(list_ammo,scrollLine,list_type_ammo):
    for ammo in list_ammo:
        y=int(ammo["pos_y"])
        print_y = scrollLine - y
        if y> scrollLine-1 or print_y+len(list_type_ammo[ammo["type"]])>36:
            ammo["on_screen"] = False

def impact(list_ammo,enemyList,list_type_ammo,player,scrollLine,obstacle_list):
        for ammo in list_ammo:
            if ammo["on_screen"]:
                if ammo["side"]==1:
                    for enemy in enemyList:
                        if enemy["alive"]:
                            if isImpactEnemy(ammo,enemy):
                                enemyLib.takeDammage(enemy,list_type_ammo[ammo["type"]]["dammagePoint"],player)
                                ammo["on_screen"]=False
                if ammo["side"]==-1 and not ammo["type"]=="big_laser_boss":
                    if isImpactAlly(ammo,player,scrollLine,int(ammo["pos_x"])):
                        PlayerLib.takeDammage(player,1)
                        ammo["on_screen"]=False
                for obstacle in obstacle_list:
                    if obstacle["alive"]:
                        if isImpactObstacle(ammo,obstacle):
                            ammo["on_screen"]=False

def isImpactEnemy(ammo,enemy):
    ammo_pos_x = ammo["pos_x"]
    ammo_last_pos_y =  ammo["last_pos_y"]
    ammo_pos_y = ammo["pos_y"]

    enemy_pos_x = enemy["pos_x"]
    enemy_pos_y = enemy["pos_y"]
    enemy_hitbox = enemy["hitbox"]
    enemy_hitbox_x,enemy_hitbox_y=enemy_hitbox

    if (ammo_pos_x>=enemy_pos_x) and (ammo_pos_x<enemy_pos_x+enemy_hitbox_x):

        ammo_inside =(ammo_pos_y>=enemy_pos_y) and (ammo_pos_y <enemy_pos_y+enemy_hitbox_y)
        ammo_passed_trought = (ammo_pos_y>enemy_pos_y) and (ammo_last_pos_y < enemy_pos_y+enemy_hitbox_y)

        if (ammo_inside or ammo_passed_trought):
            return True
    return False


def isImpactAlly(ammo,player,scrollLine,ammo_pos_x):
    ammo_last_pos_y = int(scrollLine - ammo["last_pos_y"])
    ammo_pos_y = int(scrollLine - ammo["pos_y"])

    player_pos_x = int(player["x"])
    player_pos_y = int(player["y"])
    player_hitbox = player["hitbox"]
    player_hitbox_x,player_hitbox_y=player_hitbox

    if (ammo_pos_x>=player_pos_x) and (ammo_pos_x<player_pos_x+player_hitbox_x):

        ammo_inside =(ammo_pos_y>=player_pos_y) and (ammo_pos_y <player_pos_y+player_hitbox_y)
        ammo_passed_trought = (ammo_last_pos_y < player_pos_y) and (ammo_pos_y>player_pos_y+player_hitbox_y)

        if (ammo_inside or ammo_passed_trought):
            return True
    return False

def isImpactObstacle(ammo,obstacle):
    ammo_pos_x = ammo["pos_x"]
    ammo_last_pos_y =  ammo["last_pos_y"]
    ammo_pos_y = ammo["pos_y"]

    obstacle_pos_x = obstacle["pos_x"]
    obstacle_pos_y = obstacle["pos_y"]
    obstacle_hitbox_x = obstacle["hitbox"][0]
    obstacle_hitbox_y = obstacle["hitbox"][1]

    if (ammo_pos_x>=obstacle_pos_x) and (ammo_pos_x<obstacle_pos_x+obstacle_hitbox_x):

        ammo_inside =(ammo_pos_y>=obstacle_pos_y-obstacle_hitbox_y) and (ammo_pos_y <obstacle_pos_y)#ca devrait pas fonctionner comme ca, mais ca fonctionne... donc ¯\_(ツ)_/¯
        # ammo_passed_trought_a = (ammo_pos_y>obstacle_pos_y) and (ammo_last_pos_y < obstacle_pos_y+obstacle_hitbox_y)
        # ammo_passed_trought_e = (ammo_pos_y<obstacle_pos_y) and (ammo_last_pos_y > obstacle_pos_y+obstacle_hitbox_y)

        if (ammo_inside):# or ammo_passed_trought_a or ammo_passed_trought_e):
            return True

def show(list_ammo,scrollLine,list_type_ammo):
    for ammo in list_ammo:
        if ammo["on_screen"]:
            sprite = list_type_ammo[ammo["type"]]["sprite"]

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

def initAmmoDB():
    list_type_ammo = {
    "plomb": {"sprite":["*"],"speed":2,"dammagePoint":1},
    "small_laser":{"sprite":["|"],"speed":5,"dammagePoint":1},
    "big_plomb_enemy":{"sprite":["V"],"speed":1,"dammagePoint":2},
    "big_plomb_player":{"sprite":["^"],"speed":1,"dammagePoint":2},
    "big_laser_boss":{"sprite":["¦¦","¦¦","¦¦"],"speed":0.5,"dammagePoint":2}
    }
    return list_type_ammo
