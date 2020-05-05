import hudLib
import PlayerLib
import ammoLib
import enemyLib
import enemySummonLib

def changeLevel(level_to_change,player,hud,level_list,enemySummonList,enemyList,list_ammo,scrollLine,scrollBackground,scrollBackgroundList):
    level = level_to_change

    #clear
    hudLib.initHUD_Game(hud)
    enemySummonLib.clear(enemySummonList)
    PlayerLib.setPosition(player,20,28)
    enemyLib.clearEnemyList(enemyList)
    ammoLib.clear(list_ammo)
    scrollLine = 33

    #loading
    level_data = level_list[level]

    for key in level_data["player"]:
        PlayerLib.setSomeThing(player,key,level_data["player"][key])

    PlayerLib.ComputeAndApplyHitbox(player)

    for element in level_data["enemySummonList_level"]:
        enemySummonLib.addElement(enemySummonList,element,level_data["enemySummonList_level"][element])

    scrollBackground = level_data["background"]

    level_length = level_data["length"]

    return level_length
