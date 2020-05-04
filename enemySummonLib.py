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

def summonEnemy(enemySummonList,enemyList,scrollLine,enemyDB):
    for key in enemySummonList:
        if (key <= int(scrollLine)) and (enemySummonList[key]["state"]=="waiting"):
            HP = enemyDB[enemySummonList[key]["type"]]["HP"]
            pos_x = enemySummonList[key]["pos_x"]
            pos_y = key
            sprite = enemyDB[enemySummonList[key]["type"]]["sprite"]
            color =  enemySummonList[key]["color"]
            behavior = enemySummonList[key]["behavior"]
            weapon = enemyDB[enemySummonList[key]["type"]]["weapon"]

            enemyLib.initEnemy(enemyList,HP,pos_x,pos_y,sprite,color,behavior,weapon)

            enemySummonList[key]["state"] = "summoned"

    return
