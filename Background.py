import sys
import os

#le module background gere le type abstrait de donnee background
#un background contient une chaine de caractere qui represente
#une image de fond d ecran


def create(filename):
    #creation du fond
    bg=dict()

    #ouverture fichier
    myfile = open(filename, "r")

    chaine=myfile.read()

    #separation des lignes
    listeLignes=chaine.splitlines()

    bg["map"]=[]

    #transformation en liste de liste
    for line in listeLignes:
        listeChar=list(line)
        bg["map"].append(listeChar)

    myfile.close()

    return bg

def getChar(bg,x,y):
    #renvoie le contenu d une case donnee
    return (bg["map"][y-1][x-1])

def setChar(bg,x,y,c):
    #change le contenu d une case donnee
    bg["map"][y-1][x-1]=c


def show(bg) :

    #couleur fond
    sys.stdout.write("\033[40m")
    #couleur white
    sys.stdout.write("\033[37m")

    #goto
    for y in range(0,len(bg["map"])):
        for x in range(0,len(bg["map"][y])):
            s="\033["+str(y+1)+";"+str(x+1)+"H"
            sys.stdout.write(s)
            #affiche
            sys.stdout.write(bg["map"][y][x])
