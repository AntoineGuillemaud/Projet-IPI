import enemyLib
import hudLib
import PlayerLib

def checkColision(player,enemyList,obstacle_list,scrollLine):
    checkColisionPE(player,enemyList,scrollLine)
    checkColisionPO(player,obstacle_list,scrollLine)

def checkColisionPE(player,enemyList,scrollLine):
    borne_x_player_1 = int(player["x"])
    borne_x_player_2 = int(player["x"]+player["hitbox"][0])
    borne_y_player_1 = int(scrollLine-player["y"])
    borne_y_player_2 = int(scrollLine-player["y"]+player["hitbox"][1])

    for enemy in enemyList:
        if enemy["alive"]==True:
            borne_x_obstacle_1 = enemy["pos_x"]
            borne_x_obstacle_2 = enemy["pos_x"]+enemy["hitbox"][0]
            borne_y_obstacle_1 = enemy["pos_y"]
            borne_y_obstacle_2 = enemy["pos_y"]-enemy["hitbox"][1]

            if (borne_x_player_1<borne_x_obstacle_1<borne_x_player_2) or (borne_x_player_1<borne_x_obstacle_2<borne_x_player_2) or (borne_x_obstacle_1<borne_x_player_1<borne_x_obstacle_2) or (borne_x_obstacle_1<borne_x_player_2<borne_x_obstacle_2):
                if (borne_y_player_1<borne_y_obstacle_1<borne_y_player_2) or (borne_y_player_1<borne_y_obstacle_2<borne_y_player_2) or (borne_y_obstacle_1<borne_y_player_1<borne_y_obstacle_2) or (borne_y_obstacle_1<borne_y_player_2<borne_y_obstacle_2):
                    PlayerLib.takeDammage(player,2)
                    enemy["alive"]=False



def checkColisionPO(player,obstacle_list,scrollLine):
    borne_x_player_1 = int(player["x"])
    borne_x_player_2 = int(player["x"]+player["hitbox"][0])
    borne_y_player_1 = int(scrollLine-player["y"])
    borne_y_player_2 = int(scrollLine-player["y"]+player["hitbox"][1])

    for obstacle in obstacle_list:
        if obstacle["alive"]==True:
            borne_x_obstacle_1 = obstacle["pos_x"]
            borne_x_obstacle_2 = obstacle["pos_x"]+obstacle["hitbox"][0]
            borne_y_obstacle_1 = obstacle["pos_y"]-obstacle["hitbox"][1]
            borne_y_obstacle_2 = obstacle["pos_y"]

            if (borne_x_player_1<borne_x_obstacle_1<borne_x_player_2) or (borne_x_player_1<borne_x_obstacle_2<borne_x_player_2) or (borne_x_obstacle_1<borne_x_player_1<borne_x_obstacle_2) or (borne_x_obstacle_1<borne_x_player_2<borne_x_obstacle_2):
                if (borne_y_player_1<borne_y_obstacle_1<borne_y_player_2) or (borne_y_player_1<borne_y_obstacle_2<borne_y_player_2) or (borne_y_obstacle_1<borne_y_player_1<borne_y_obstacle_2) or (borne_y_obstacle_1<borne_y_player_2<borne_y_obstacle_2):
                    PlayerLib.takeDammage(player,2)
                    obstacle["alive"]=False
