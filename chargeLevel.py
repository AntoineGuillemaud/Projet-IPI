import enemyDBLib


def ChargeLevelIntoRAM(sprites,scrollBackgroundList):

     level_list = list()



     level0={}
     level_list.append(level0)


     level1 = {
     "background" : scrollBackgroundList["level1"],
     "enemySummonList_level" : {
        40:{"type":"weak","pos_x":20,"behavior":None,"color":2 , "state":"waiting"},
        60:{"type":"weak","pos_x":20,"behavior":None,"color":2 , "state":"waiting"}
        },
    "player":{
        "color":4,
        "direction":"null",
        "x":5.0,
        "y":5.0,
        "speed":6.0,
        "sprite":sprites["little_ship"]
        },
    "length" : 195
     }
     level_list.append(level1)


     return level_list
