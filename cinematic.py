#>--------------<#
# obstacle.py    #
# M****** N****  #
# 03/06/2020     #
# S2P- C- 05     #
#>--------------<#

import sys
import os
import time

def create(filename):

    animation=dict()

    #recuperation du film
    myfile = open(filename, "r")
    chaine = myfile.read()

    #separation des frames
    frames = chaine.split("frame\n")

    animation["frames"]=[]
    for f in frames:
        animation["frames"].append(f)

    animation["timeStep"] = 5

    return animation


def showFrame(cinematic, rank) :
    assert type(cinematic) is dict
    assert type(rank) is int

    #couleur fond noire
    sys.stdout.write("\033[40m")

    #couleur animation
    txt="\033[37m"
    sys.stdout.write(txt)

    #affichage de la frame
    sys.stdout.write("\033[0;0H\n")
    sys.stdout.write(cinematic["frames"][rank])

def showEntireCinematic(cinematic) :
    assert type(cinematic) is dict

    for i in range(0, len(cinematic["frames"]) - 1) :
        showFrame(cinematic, i)
        time.sleep(cinematic["timeStep"])

    return
