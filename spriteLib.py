################
# sprite.py    #
# A.Guillemaud #
# 02/04/2020   #
# S2-P IPI     #
################


def initSprites(filename):

    sprites = dict()

    myFile = open(filename, 'r')
    fileContent = myFile.read()

    sprites_list = fileContent.split("\nsprite\n")

    for sprite_raw in sprites_list:
        sprite_lines = sprite_raw.split("\n")
        sprite_name = sprite_lines[0]
        del sprite_lines[0]
        sprites[sprite_name]=[]
        for sprite_line in sprite_lines:
            sprites[sprite_name].append(sprite_line)

    return sprites
