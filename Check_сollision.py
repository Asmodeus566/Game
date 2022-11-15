from Game_player import *
from Game_enemy import *
"""
В этом файле находятся функции преследования игрока, и проверка столкновения его с противником
"""
                                                                # проверка столконовения игрока с проивником:
def check_collision(player, enemy, shado):

    p_bottom =  player.check_bottom()
    p_left =    player.check_left()
    p_right =   player.check_right()
    p_top =     player.check_top()

    e_bottom =  enemy.check_bottom()
    e_top =     enemy.check_top()
    e_right =   enemy.check_right()
    e_left =    enemy.check_left()

    s_right =   shado.check_right()
    s_top =     shado.check_top()
    s_bottom =  shado.check_bottom()
    s_left =    shado.check_left()

    died =      False
    if enemy.check_died() == False:
        if (p_bottom == e_bottom and p_right >= e_left and p_left <= e_right):
            died = True


    if shado.check_shot() or shado.check_long_punch():
        if p_right >= s_left:
            died = True

    return died

                                                                # Настройка преследования игрока врагом:
def player_pursuit(player, enemy):
    position        = [0,0]

    player_right    = player.check_right()
    player_bottom   = player.check_bottom()

    enemy_right     = enemy.check_right()
    enemy_bottom    = enemy.check_bottom()

    if enemy_bottom > player_bottom:                            # Если противник выше чем игрот отнимаем 2 по Y
        position[1] = -2                                        # Записать в список
    if enemy_bottom < player_bottom:                            # Если противник ниже чем игрот прибавляем 2 по Y
        position[1] = 2                                         # Записать в список
    if enemy_bottom == (player_bottom-1 or player_bottom + 1):
        enemy.set_bottom(player_bottom)
    if enemy_bottom == player_bottom:                           # Если по Y спрайты на одной позиции то прекратить движение по Y
        position[1] = 0                                         # Записать в список
    if enemy_right > player_right:                              # Если противник справо от игрока отнимать 2 по X
        position[0] = -2                                        # Записать в список
    if enemy_right < player_right:                              # Если противник слево от игрока прибавляем 2 по X
        position[0] = 2                                         # Записать в список
    if enemy_right == player_right:                             # Если сравнялись прекратить ходьбу
        position[0] = 0                                         # Записать в список

    return position                                             # Вернуть список
