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

def summonEnemy(enemySummonList,enemyList,scrollLine):
    for key in enemySummonList:
        if key <= scrollLine:
            HP = enemyDB[enemySummonList[key]["type"]]["HP"]
            pos_x = enemySummonList[key]["pos_x"]
            sprite = enemyDB[enemySummonList[key]["type"]]["sprite"]
            color =  enemySummonList[key]["color"]
            behavior = enemySummonList[key]["behavior"]
            weapon = enemyDB[enemySummonList[key]["type"]]["weapon"]

            enemyLib.initEnemy(enemyList,HP,pos_x,sprite,color,behavior,weapon)
    return
