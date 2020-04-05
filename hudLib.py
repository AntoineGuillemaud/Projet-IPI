################
# sprite.py    #
# A.Guillemaud #
# 02/04/2020   #
# S2-P IPI     #
################

import sys

def initHUD():
    hud = dict()
    hud["vies"] = {"value":0,"pos_x":9,"pos_y":36,"color":1}
    hud["ammo"] = {"value":0,"pos_x":30,"pos_y":36,"color":1}
    hud["special1"] = {"value":0,"pos_x":14,"pos_y":37,"color":1}
    hud["special2"] = {"value":0,"pos_x":35,"pos_y":37,"color":1}
    return hud


def showHUD(hud):
    for key in hud:
        value = hud[key]["value"]
        pos_x = hud[key]["pos_x"]
        pos_y = hud[key]["pos_y"]
        color = hud[key]["color"]

        sys.stdout.write("\033[40m")
        txt="\033[3"+str(color%7+1)+"m"
        sys.stdout.write(txt)
        txt="\033["+str(pos_y)+";"+str(pos_x)+"H"
        sys.stdout.write(txt)
        sys.stdout.write(str(value))
    return