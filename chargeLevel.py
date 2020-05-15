import enemyDBLib


def ChargeLevelIntoRAM(sprites,scrollBackgroundList,Behaviors):

     level_list = list()



     level0={}
     level_list.append(level0)


     level1 = {
     "background" : scrollBackgroundList["level1"],
     "enemySummonList_level" : {
        40:{"type":"weak","pos_x":10,"behavior":Behaviors["random"],"color":2 , "state":"waiting"},
        42:{"type":"weak","pos_x":20,"behavior":Behaviors["random"],"color":2 , "state":"waiting"},
        44:{"type":"weak","pos_x":30,"behavior":Behaviors["random"],"color":2 , "state":"waiting"},
        46:{"type":"weak","pos_x":15,"behavior":Behaviors["random"],"color":2 , "state":"waiting"},
        48:{"type":"weak","pos_x":25,"behavior":Behaviors["random"],"color":2 , "state":"waiting"},
        50:{"type":"weak","pos_x":35,"behavior":Behaviors["random"],"color":2 , "state":"waiting"},
        52:{"type":"weak","pos_x":21,"behavior":Behaviors["random"],"color":2 , "state":"waiting"},
        54:{"type":"weak","pos_x":7,"behavior":Behaviors["random"],"color":2 , "state":"waiting"},
        60:{"type":"weak","pos_x":17,"behavior":Behaviors["random"],"color":2 , "state":"waiting"}
        },
    "player":{
        "color":4,
        "direction":"null",
        "x":20.0,
        "y":28.0,
        "speed":6.0,
        "sprite":sprites["little_ship"]
        },
    "length" : 195
     }
     level_list.append(level1)


     return level_list
