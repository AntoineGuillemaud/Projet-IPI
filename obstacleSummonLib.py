import obstacleLib

def init():
    obstacleSummon_list=dict()
    return obstacleSummon_list

def clear(obstacleSummon_list):
    obstacleSummon_list.clear()

def addElement(obstacleSummon_list,key,value):
    obstacleSummon_list[key]=dict(value)

def summonObstacle(obstacleSummon_list,obstacle_list,scrollLine):
    for key in obstacleSummon_list:
        if (key <= int(scrollLine)) and (obstacleSummon_list[key]["state"]=="waiting"):
            pos_x = obstacleSummon_list[key]["pos_x"]
            pos_y = key
            sprite = obstacleSummon_list[key]["sprite"]
            color =  obstacleSummon_list[key]["color"]

            obstacleLib.addObstacle(obstacle_list,pos_x,pos_y,sprite,color)

            obstacleSummon_list[key]["state"] = "summoned"

    return
