import hudLib
import PlayerLib
import ammoLib
import enemyLib
import enemySummonLib

def changeLevel(level_to_change,player,hud,level_list,enemySummonList,enemyList,list_ammo,scrollLine):
    level = level_to_change
    clearLevel(player,list_ammo,enemyList,hud,enemySummonList,scrollLine)
    loadLevel(level,player,hud,level_list,enemySummonList)
    return level

def clearLevel(player,list_ammo,enemyList,hud,enemySummonList,scrollLine):
    hudLib.initHUD_Game(hud)
    enemySummonLib.clear(enemySummonList)
    PlayerLib.setPosition(player,5,5)
    #pos background
    enemyLib.clearEnemyList(enemyList)
    ammoLib.clear(list_ammo)
    scrollLine = 33
    return

def loadLevel(level,player,hud,level_list,enemySummonList):

    level_data = level_list[level]

    for key in level_data["player"]:
        PlayerLib.setSomeThing(player,key,level_data["player"][key])

    PlayerLib.ComputeAndApplyHitbox(player)

    for element in level_data["enemySummonList_level"]:
        enemySummonLib.addElement(enemySummonList,element,level_data["enemySummonList_level"][element])

    level_length = level_data["length"]

    return level_length
