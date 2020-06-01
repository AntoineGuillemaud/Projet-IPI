import enemyDBLib


def ChargeLevelIntoRAM(sprites,scrollBackgroundList,Behaviors):

     level_list = list()

     default_behavior_param = {"last_move":float(0.0),"speed":2,"move_state":0}

     level0={}
     level_list.append(level0)


     level1 = {
     "background" : scrollBackgroundList["level1"],
     "enemySummonList_level" : {
        20:{"type":"weak","pos_x":10,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":5,"color":2 , "state":"waiting"},
        45:{"type":"weak","pos_x":15,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":5,"color":2 , "state":"waiting"},
        50:{"type":"weak","pos_x":20,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":5,"color":2 , "state":"waiting"},
        55:{"type":"weak","pos_x":25 ,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":4,"color":2 , "state":"waiting"},
        60:{"type":"weak","pos_x":30,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":4,"color":2 , "state":"waiting"}
        },
    "obstacleSummonList_level":{
        35:{"pos_x":20,"sprite":sprites["obstacle_small_asteroide"],"color":6, "state":"waiting"}
    },
    "player":{
        "color":1,
        "direction":"null",
        "x":20.001,
        "y":28.0,
        "speed":6.0,
        "sprite":sprites["little_ship"],
        "ammo_quantity":99,
        "ammo_type":"small_laser",
        "HP":5,
        "capacity_1":None,
        "shooting":False,
        "last_cooldown_scrollLine":33
        },
    "length" : 195
     }
     level_list.append(level1)



     return level_list
