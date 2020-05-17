import enemyLib

def init():
    enemySummonList=dict()
    return enemySummonList

def clear(enemySummonList):
    enemySummonList=dict()
    return

def addElement(enemySummonList,key,value):
    enemySummonList[key]=value
    return

def summonEnemy(enemySummonList,enemyList,scrollLine,enemy_types):
    for key in enemySummonList:
        if (key <= int(scrollLine)) and (enemySummonList[key]["state"]=="waiting"):
            HP = enemy_types[enemySummonList[key]["type"]]["HP"]
            pos_x = enemySummonList[key]["pos_x"]
            pos_y = key
            sprite = enemy_types[enemySummonList[key]["type"]]["sprite"]
            color =  enemySummonList[key]["color"]
            behavior = enemySummonList[key]["behavior"]
            behavior_param = enemySummonList[key]["behavior_param"]
            weapon = enemy_types[enemySummonList[key]["type"]]["weapon"]
            cooldown = enemySummonList[key]["cooldown"]

            enemyLib.initEnemy(enemyList,HP,pos_x,pos_y,sprite,color,behavior,behavior_param,weapon,cooldown)

            enemySummonList[key]["state"] = "summoned"

    return
