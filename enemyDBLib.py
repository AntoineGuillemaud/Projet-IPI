import spriteLib
import enemyLib
import random
#Behaviors
def behavior_left_right(enemy):
    enemyLib.move_direction(enemy,1,1)

def behavior_random(enemy):
    enemyLib.move_direction(enemy,random.randint(0,1)*2-1,1)

#Init
def init(sprites):
    enemy_types = init_enemy_types(sprites)
    enemy_behaviors =init_enemy_behavior()
    return (enemy_types,enemy_behaviors)

def init_enemy_types(sprites):
    enemy_types = {
        "weak": {"HP":1,"sprite":sprites["enemy_ship_weak"],"weapon":None}

        }
    return enemy_types

def init_enemy_behavior():
    enemy_behaviors = {
        "left_right" : behavior_left_right,
        "random" : behavior_random
        }
    return enemy_behaviors
