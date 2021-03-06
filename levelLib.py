import hudLib
import PlayerLib
import ammoLib
import enemyLib
import enemySummonLib
import obstacleLib
import obstacleSummonLib

def changeLevel(level_to_change,player,hud,level_list,enemySummonList,enemyList,list_ammo,scrollLine,scrollBackground,scrollBackgroundList,obstacle_list,obstacleSummon_list):
    level = level_to_change

    #clear
    hudLib.initHUD_Game(hud)
    enemySummonLib.clear(enemySummonList)
    PlayerLib.setPosition(player,20,28)
    enemyLib.clearEnemyList(enemyList)
    ammoLib.clear(list_ammo)
    obstacleLib.clear(obstacle_list)
    scrollLine = 33

    #loading
    print(level)
    level_data = dict(level_list[level])

    for key in level_data["player"]:
        PlayerLib.setSomeThing(player,key,level_data["player"][key])

    PlayerLib.ComputeAndApplyHitbox(player)

    for element in level_data["enemySummonList_level"]:
        enemySummonLib.addElement(enemySummonList,element,level_data["enemySummonList_level"][element])

    for element in level_data["obstacleSummonList_level"]:
        obstacleSummonLib.addElement(obstacleSummon_list,element,level_data["obstacleSummonList_level"][element])

    for i in range(0,len(level_data["background"])): #C'est vraiment super sale comme facons de faire les choses mais il est 21h57 et on doit rendre le projet a 23h55 donc 
        scrollBackground[i]=level_data["background"][i]

    level_length = level_data["length"]

    return level_length,scrollLine
