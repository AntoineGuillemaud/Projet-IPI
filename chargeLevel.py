import enemyDB


def ChargeLevelIntoRAM(sprites):

     level_list = list()

     level0={}
     level_list.append(level0)


     level1 = {
     "background" : "resources/background_level1.txt",
     "enemySummonList_level" : {
        50:enemyDB.summon_weak,
        60:enemyDB.summon_weak
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
