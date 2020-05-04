
def create():

    list_ammo = list()

    return list_ammo

def clear(list_ammo):
    list_ammo.clear()

def appendAmmo(list_ammo,type,pos_x,pos_y,speed,side,color,carac1=None,carac2=None):

    ammo = dict()
    ammo["type"]=type
    ammo["pos_x"] = pos_x
    ammo["pos_y"] = pos_y
    ammo["speed"] = speed
    ammo["side"] = side
    ammo["color"] = color
    ammo["carac1"] = carac1
    ammo["carac2"] = carac2

    list_ammo.append(ammo)
    return

def move(list_ammo):
    for ammo in list_ammo:
        if ammo["type"] == "plomb":
            ammo["pos_y"] = ammo["pos_y"] + 1 * side * speed
    return


def impact(list_ammo):
    return

def show(list_ammo):
    for ammo in list_ammo:
        if ammo["type"] == "plomb":
            sprite = ["*"]

        x=int(ammo["pos_x"])
        y=int(ammo["pos_y"])

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
    return
