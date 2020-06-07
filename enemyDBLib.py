import spriteLib
import enemyLib
import random
#Behaviors
def behavior_left_right_4t(enemy,scrollLine):
    codex={0:1,1:-1,2:-1,3:1}
    behavior_param = enemy["behavior_param"]
    enemy_last_move_time = ((scrollLine-behavior_param["last_move"])*behavior_param["speed"])
    if enemy_last_move_time>=2.6:
        behavior_param["last_move"]=scrollLine
        enemyLib.move_direction(enemy,1,codex[behavior_param["move_state"]])
        behavior_param["move_state"]=(behavior_param["move_state"]+1)%4

def behavior_left_right_40t(enemy,scrollLine):
    codex={0:2,1:2,2:2,3:2,4:2,5:2,6:2,7:2,8:2,9:2,10:2,11:2,12:-2,13:-2,14:-2,15:-2,16:-2,17:-2,18:-2,19:-2,20:-2}
    behavior_param = enemy["behavior_param"]
    enemy_last_move_time = ((scrollLine-behavior_param["last_move"])*behavior_param["speed"])
    if enemy_last_move_time>=4:
        behavior_param["last_move"]=scrollLine
        enemyLib.move_direction(enemy,1,codex[behavior_param["move_state"]])
        behavior_param["move_state"]=(behavior_param["move_state"]+1)%20

def behavior_random(enemy,scrollLine):
    enemy_last_move_time = ((scrollLine-enemy["behavior_param"]["last_move"])*enemy["behavior_param"]["speed"])
    if enemy_last_move_time >= 2.5:
        enemyLib.move_direction(enemy,random.randint(0,1)*2-1,1)
        enemy["behavior_param"]["last_move"]=scrollLine

def behavior_stay_still(enemy,scrollLine):
    DoNothing=True

#Init
def init(sprites):
    enemy_types = init_enemy_types(sprites)
    enemy_behaviors =init_enemy_behavior()
    return (enemy_types,enemy_behaviors)

def init_enemy_types(sprites):
    enemy_types = {
        "weak": {"HP":1,"sprite":sprites["enemy_ship_weak"],"score_value":100,"weapon":{"ammo_type":"plomb","cooldown_rate":0.1}},
        "final_boss": {"HP":50,"sprite":sprites["final_boss"],"score_value":5000,"weapon":{"ammo_type":"big_laser_boss","cooldown_rate":1}}

        }
    return enemy_types

def init_enemy_behavior():
    enemy_behaviors = {
        "behavior_left_right_4t" : behavior_left_right_4t,
        "random" : behavior_random,
        "stay_still":behavior_stay_still,
        "behavior_left_right_40t": behavior_left_right_40t
        }
    return enemy_behaviors
