import spriteLib
import enemyLib
import random
#Behaviors
def behavior_left_right(enemy):
    enemyLib.move_direction(enemy,1,1)

def behavior_random(enemy,scrollLine):
    enemy_last_move_time = ((scrollLine-enemy["behavior_param"]["last_move"])*enemy["behavior_param"]["speed"])
    if enemy_last_move_time >= 2.5:
        enemyLib.move_direction(enemy,random.randint(0,1)*2-1,1)
        enemy["behavior_param"]["last_move"]=scrollLine

#Init
def init(sprites):
    enemy_types = init_enemy_types(sprites)
    enemy_behaviors =init_enemy_behavior()
    return (enemy_types,enemy_behaviors)

def init_enemy_types(sprites):
    enemy_types = {
        "weak": {"HP":1,"sprite":sprites["enemy_ship_weak"],"weapon":{"ammo_type":"plomb","cooldown_rate":0.1}}

        }
    return enemy_types

def init_enemy_behavior():
    enemy_behaviors = {
        "left_right" : behavior_left_right,
        "random" : behavior_random
        }
    return enemy_behaviors
