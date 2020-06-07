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
        88:{"type":"weak","pos_x":20,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":1,"color":2 , "state":"waiting"},
        89:{"type":"weak","pos_x":36,"behavior":Behaviors["behavior_left_right_4t"],"behavior_param":dict(default_behavior_param),"cooldown":3,"color":2 , "state":"waiting"},
        90:{"type":"weak","pos_x":13,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":2,"color":2 , "state":"waiting"},
        91:{"type":"weak","pos_x":27,"behavior":Behaviors["stay_still"],"behavior_param":dict(default_behavior_param),"cooldown":4,"color":2 , "state":"waiting"},
        124:{"type":"weak","pos_x":15,"behavior":Behaviors["behavior_left_right_4t"],"behavior_param":dict(default_behavior_param),"cooldown":3,"color":2 , "state":"waiting"},
        138:{"type":"weak","pos_x":27,"behavior":Behaviors["behavior_left_right_4t"],"behavior_param":dict(default_behavior_param),"cooldown":4,"color":2 , "state":"waiting"},
        139:{"type":"weak","pos_x":35,"behavior":Behaviors["behavior_left_right_4t"],"behavior_param":{"last_move":float(0.0),"speed":2.5,"move_state":2},"cooldown":1,"color":2 , "state":"waiting"}
        },
    "obstacleSummonList_level":{
        36:{"pos_x":32,"sprite":sprites["obstacle_small_asteroide"],"color":6, "state":"waiting"},
        43:{"pos_x":20,"sprite":sprites["obstacle_asteroid_1"],"color":6, "state":"waiting"},
        57:{"pos_x":5,"sprite":sprites["obstacle_asteroid_3"],"color":6, "state":"waiting"},
        72:{"pos_x":18,"sprite":sprites["obstacle_asteroid_2"],"color":6, "state":"waiting"},
        73:{"pos_x":30,"sprite":sprites["obstacle_asteroid_6"],"color":6, "state":"waiting"},
        96:{"pos_x":2,"sprite":sprites["obstacle_small_asteroide"],"color":6, "state":"waiting"},
        98:{"pos_x":15,"sprite":sprites["obstacle_scrap"],"color":6, "state":"waiting"},
        99:{"pos_x":33,"sprite":sprites["obstacle_small_asteroide"],"color":6, "state":"waiting"},
        105:{"pos_x":5,"sprite":sprites["obstacle_asteroid_4"],"color":6, "state":"waiting"},
        107:{"pos_x":30,"sprite":sprites["obstacle_asteroid_5"],"color":6, "state":"waiting"},
        108:{"pos_x":15,"sprite":sprites["obstacle_asteroid_4"],"color":6, "state":"waiting"},
        112:{"pos_x":35,"sprite":sprites["obstacle_asteroid_4"],"color":6, "state":"waiting"},
        114:{"pos_x":4,"sprite":sprites["obstacle_asteroid_4"],"color":6, "state":"waiting"},
        117:{"pos_x":24,"sprite":sprites["obstacle_asteroid_3"],"color":6, "state":"waiting"},
        123:{"pos_x":35,"sprite":sprites["obstacle_asteroid_6"],"color":6, "state":"waiting"},
        125:{"pos_x":3,"sprite":sprites["obstacle_asteroid_4"],"color":6, "state":"waiting"},
        127:{"pos_x":18,"sprite":sprites["obstacle_asteroid_7"],"color":6, "state":"waiting"},
        129:{"pos_x":10,"sprite":sprites["obstacle_asteroid_3"],"color":6, "state":"waiting"},
        131:{"pos_x":22,"sprite":sprites["obstacle_asteroid_4"],"color":6, "state":"waiting"},
        141:{"pos_x":24,"sprite":sprites["obstacle_asteroid_5"],"color":6, "state":"waiting"},
        144:{"pos_x":32,"sprite":sprites["obstacle_asteroid_8"],"color":6, "state":"waiting"},
        145:{"pos_x":4,"sprite":sprites["obstacle_asteroid_2"],"color":6, "state":"waiting"},
        159:{"pos_x":38,"sprite":sprites["obstacle_asteroid_4"],"color":6, "state":"waiting"}
    },
    "player":{
        "color":1,
        "direction":"null",
        "x":20.001,
        "y":24.0,
        "speed":6.0,
        "sprite":sprites["little_ship"],
        "ammo_quantity":999,
        "ammo_type":"small_laser",
        "HP":10,
        "capacity_1":None,
        "shooting":False,
        "last_cooldown_scrollLine":33
        },
    "length" : 190
     }
     level_list.append(level1)







     return level_list
