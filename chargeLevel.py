import enemyDBLib


def ChargeLevelIntoRAM(sprites,scrollBackgroundList,Behaviors):

     level_list = list()

     default_behavior_param = {"last_move":float(0.0),"speed":2,"move_state":0}

     level0={}
     level_list.append(level0)


     level1 = {
     "background" : scrollBackgroundList["level1"],
     "enemySummonList_level" : {
        45:{"type":"weak","pos_x":10,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":1,"color":2 , "state":"waiting"},
        54:{"type":"weak","pos_x":12,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":4,"color":2 , "state":"waiting"},
        66:{"type":"weak","pos_x":33,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":4,"color":2 , "state":"waiting"},
        67:{"type":"weak","pos_x":23,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":4,"color":2 , "state":"waiting"},
        88:{"type":"weak","pos_x":20,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":4,"color":2 , "state":"waiting"},
        89:{"type":"weak","pos_x":36,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":4,"color":2 , "state":"waiting"},
        90:{"type":"weak","pos_x":13,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":4,"color":2 , "state":"waiting"},
        91:{"type":"weak","pos_x":27,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":4,"color":2 , "state":"waiting"}
        },
    "obstacleSummonList_level":{
        36:{"pos_x":32,"sprite":sprites["obstacle_small_asteroide"],"color":6, "state":"waiting"},
        43:{"pos_x":20,"sprite":sprites["obstacle_small_asteroide"],"color":6, "state":"waiting"},
        61:{"pos_x":4,"sprite":sprites["obstacle_small_asteroide"],"color":6, "state":"waiting"},
        75:{"pos_x":18,"sprite":sprites["obstacle_small_asteroide"],"color":6, "state":"waiting"},
        76:{"pos_x":31,"sprite":sprites["obstacle_small_asteroide"],"color":6, "state":"waiting"},
        96:{"pos_x":2,"sprite":sprites["obstacle_small_asteroide"],"color":6, "state":"waiting"},
        97:{"pos_x":30,"sprite":sprites["obstacle_small_asteroide"],"color":6, "state":"waiting"},
        98:{"pos_x":14,"sprite":sprites["obstacle_small_asteroide"],"color":6, "state":"waiting"},
        990:{"pos_x":32,"sprite":sprites["obstacle_small_asteroide"],"color":6, "state":"waiting"},
        430:{"pos_x":20,"sprite":sprites["obstacle_small_asteroide"],"color":6, "state":"waiting"}
    },
    "player":{
        "color":1,
        "direction":"null",
        "x":20.001,
        "y":24.0,
        "speed":6.0,
        "sprite":sprites["little_ship"],
        "ammo_quantity":99,
        "ammo_type":"small_laser",
        "HP":10,
        "capacity_1":None,
        "shooting":False,
        "last_cooldown_scrollLine":33
        },
    "length" : 275
     }
     level_list.append(level1)



     return level_list
