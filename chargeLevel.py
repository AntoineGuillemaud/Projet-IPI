import enemyDBLib


def ChargeLevelIntoRAM(sprites):

     level_list = list()



     level0={}
     level_list.append(level0)


     level1 = {
     "background" : "resources/background_level1.txt",
     "enemySummonList_level" : {
        50:{"type":"weak","pos_x":20,"behavior":None,"color":1},
        60:{"type":"weak","pos_x":20,"behavior":None, "color":1}
        },
    "player":{
        "color":4,
        "direction":"null",
        "x":5.0,
        "y":5.0,
        "speed":6.0,
        "sprite":sprites["little_ship"]
        },
    "length" : 200
     }
     level_list.append(level1)



     return level_list
