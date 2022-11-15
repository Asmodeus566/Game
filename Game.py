#23 секунды => 13-14 секунд
from Quests import *
import time as timet
from random import *
from moviepy.editor import *
from Game_texture import *
from Game_player import *
from Game_enemy import *
from Check_сollision import *
from Game_replic import *
import pygame
#pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
from sys import *
#Импорт необходимых кнопок
from pygame.locals import *


"""
Главный фаил игры объединяющий всё
P.s Шрифты:
Blaze.ttf - Shado(обычный)
Manga.ttf - Игрок и двери
SehnsuchtFont.ttf - Shado(злой)
"""

name = ''
game_restart = False
                                                #Игровой цикл
def main():
    global name, game_restart


    repliks                 = {0: [[1, 3, 2], False, False], 1: [[1, 1, 1], False, False], 2: [[1, 2, 0], False, False],
                               5: [[3,6, 0], False, False], 12: [[1, 2, 0]] }
    replic_level            = [0, 1, 2, 5, 12]
    player_replic_ask       = 0
    shado_replic_ask        = 0
    end_replic              = {0: False, 1: False, 2: False , 5: False, 12: False}

    SCREEN_WIDTH        = 1280
    SCREEN_HEIGHT       = 1024
                                                    # Ограничения хождения игрока вверх и вниз:
    TOP_USER_WALK       = 550                             # Верхнее ограничение
    MIN_USER_WALK       = 1024                            # Нижнее ограничение
    pygame.font.init()
                                                    # Частота кадров в секунду: Регулирование скорости игры
    FPS = 60
    LEF = 0                                         # <- ровень игрока
                                                    # Текст
    font_idle           = pygame.font.SysFont('Arial', 20)
    font                = pygame.font.Font('font/Manga.ttf', 30)
    shado_font          = pygame.font.Font('font/Blaze.ttf', 20)
    shado_engry_font    = pygame.font.Font('font/SehnsuchtFont.ttf', 30)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

                                                    # icon = pygame.display.set_icon('')
    pygame.display.set_caption('Hospital survival quest')

    # Воспроизведение видео в игре
    # clip = VideoFileClip(r"test.mp4")
    # clip.preview()
    # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                                                    # Музыка для игры:
    music = {"Menu_music": 'music\Background.mp3', "Background_music": "music\Bg.mp3"}


                                                    # инвентарь:

    Ivent_panel = IventPanel()
    user_ivent  = User_ivent()

                                                    # Меню
    menu        = True
    settings    = False
    info        = False
    game_pause = False                              # Контроль паузы игры

                                                    # Музыка:

    s       = pygame.mixer.Sound("music/Background.ogg")
    s2      = pygame.mixer.Sound("music/Background.ogg")

    s.play(-1)


                                                    # Контроль активности карты
    map_on = False

                                                    # Группы спрайтов для игрока и противников
    player_sprite   = pygame.sprite.Group()           # Игрок
    enemy_sprite    = pygame.sprite.Group()            # Противники
    door_list       = pygame.sprite.Group()
                                                    # Игрок и противники
    player  = Player(LEF)
    enemy   = Enemy()

                                                    # Карта
    map     = Map()

    lives   = UserHealts()                            # жизни

    stat    = User_Stat()
                                                    #Дверь
    door    =  Door()
    door_2  = Door()
                                                    #Реплики:
    Replic_windows = Replic_window()


                                                    #Квесты:

    quest       = Quests()
    password    = []
    for i in range(5):
        n = random.randint(0,9)
        password.append(str(n))
    Satan_password = PasswordNumber(password)
    password = ("".join(password[0:5]))
    print(password)

    quest_1 = Quest_1(int(password))
    quest_password_num = Quests_number_print()
    #quest_level = [0, 3, 8 ,10, 13]
    quest_level = [0, 3]

    shado = Shado()


                                                    # Добавление игроков и противников в группы спрайтов
    player_sprite.add(player)
    enemy_sprite.add(enemy)
    door_list.add(door)



                                                    # Контролирование скорости игры
    clock = pygame.time.Clock()
                                                    # Контроль игрового цикла
    run = True

    dead =      0
    levels_door =    [0, 8, 9, 10]


    while run:                                      # Главный цикл игры

        if menu and not game_restart:                                    # Меню
            men = Menu()                            # Определения класса меню


            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos_x = event.pos[0]
                        pos_y = event.pos[1]
                                                           #Проверка где находится мышь при нажатие
                        if (pos_x >= 40 and pos_x <= 270) and (pos_y >= 240 and pos_y <= 300):
                            menu = False                    # Выход из меню начало игры
                            player.set_pause(False)
                            #s.stop()
                            #s2.play(-1)
                        elif (pos_x >= 40 and pos_x <= 425) and (pos_y >= 350 and pos_y <= 420):
                            menu = False                    # Выход из меню переход в настройки
                            settings = True
                        elif (pos_x >= 40 and pos_x <= 320) and (pos_y >= 465 and pos_y <= 525):
                            menu = False                    # Выход из меню в раздел информации
                            info = True
                        elif (pos_x >= 40 and pos_x <= 260) and (pos_y >= 555 and pos_y <= 620):
                            pygame.quit()                   # Выход из игры

            screen.blit(men.image, men.rect)
            pygame.display.flip()

                                                                #Настройки игры
        elif settings:
            set = Settings()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        settings = False
                        menu = True
            screen.blit(set.image, set.rect)
            pygame.display.flip()

                                                                    #Информация о игре
        elif info:
            inf = Info()
                                                                    # Проверка нажатий
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        info = False
                        menu = True

            screen.blit(inf.image, inf.rect)
            pygame.display.flip()

        elif game_pause:
            pause = Game_pause()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_TAB:
                        game_pause = False
                        player.set_pause(False)

            screen.blit(pause.image, pause.rect)
            pygame.display.flip()



        else:
                                                         # Ьузыка для фона

            # Получение нажатий на кнопки:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        #game_pause = True
                        menu = True
                        player.set_pause(True)
                    if event.key == K_TAB:
                        map_on = True
                elif event.type == KEYUP:
                    if event.key == K_TAB:
                        s.stop()
                        map_on = False # Открываем карту

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos_x = event.pos[0]
                        pos_y = event.pos[1]
                        print(f"X: {pos_x}, Y: {pos_y}")


                elif event.type == QUIT:
                    run = False # Заканчиваем игру

        #Получение нажатой кнопки
            key_pressed     = pygame.key.get_pressed()
            player_run      = player.check_run()
            stat_yes        = stat.check_stat()

            a               = player.check_bottom() # Проверка нижнего положения игрока
            a2              = player.check_right() # Проверка правого положения игрока
            Shado_bottom    = shado.check_bottom()

            if dead == 25:
                run = False

            check = check_collision(player, enemy, shado) # Проверка столкновения
            if check == 1:
                run = False

            # Изображения заднего фона
            l       = player.check_level() # Проверка уровня игрока
            wall    = unfisiball_wall(l)

            # Смена изображений при смене уровня

            im = Photo_load(l, a, a2) # Получение изображение

            BackGround = Background(im, [0, 0]) # Смена заднего фона

            screen.blit(BackGround.image, BackGround.rect) # Установка фона

            if l == 2:              # Отрисовка пароля на пентаграмме
                screen.blit(Satan_password.image1, Satan_password.rect1)
                screen.blit(Satan_password.image2, Satan_password.rect2)
                screen.blit(Satan_password.image3, Satan_password.rect3)
                screen.blit(Satan_password.image4, Satan_password.rect4)
                screen.blit(Satan_password.image5, Satan_password.rect5)

            # оТРИСОВКА ДВЕРИ:
            if l in levels_door:
                pos = door_position(l)

                door_list.update(pos, l, player, quest_1)
                door_list.draw(screen)
            # Вторая дверь

            #if l == 1:
                #door_2.update([800, 620], l, player)          #Обновление второй дверии
                #screen.blit(door_2.image, door_2.rect)
            # Квесты и их расположение
            if l in quest_level:
                quest_position = quest_pos(l)
                quest.update(quest_position, l)
                screen.blit(quest.image, quest.rect)

            if a > Shado_bottom and l == 5:                    #если Shado выше игрока, то отобрадаем его первее
                screen.blit(shado.image, shado.rect)           #чтобы игрок его перекрывал, и создавалось ощущение объема
                shado.update(key_pressed, player)


            if player.check_bottom() < enemy.check_bottom():   #Отображение игрока поверх противника
                player_sprite.update(key_pressed, stat_yes, stat.check_full_stat_use(), door, quest_1, user_ivent.check_ivent_all(), shado, wall)
                player_sprite.draw(screen)                     #Отрисовка игрока

            if l == 5 or l == 0:
                enemy_sprite.update(player, enemy)
                enemy_sprite.draw(screen)

            else:
                enemy.set_dead(True)

            if player.check_bottom() >= enemy.check_bottom(): #Отображение игрока за  противником
                player_sprite.update(key_pressed, stat_yes, stat.check_full_stat_use(), door, quest_1, user_ivent.check_ivent_all(), shado, wall)
                player_sprite.draw(screen)

            text = text_on(door, door_2, l, player)
                                                                # Получение текста при необходимости
            x_text, y_text = text_pos(door, door_2)
            if text != None:                                     # Вывод текста если необходимо
                text = font.render(text, False, [46, 2, 2])
                screen.blit(text, (x_text, y_text))


            lives.healts_update(lives=dead)                       # Отображение и обновление здоровья
            screen.blit(lives.image, lives.rect)

            stat.update(run=player_run)                          # Отображение и обновления статы
            screen.blit(stat.image, stat.rect)
            if l in quest_level:                                # Если игрок в уровне с квестом и его координаты совпадают с квестом

                if (player.rect.right >= quest.rect.left - 5 and player.rect.right <= quest.rect.right + 5  and player.rect.bottom <= 650)\
                or (player.rect.left <= quest.rect.right + 5  and player.rect.left >= quest.rect.left - 5 and player.rect.bottom <= 650) :
                    if l == 0 and not quest_1.quest_end:
                        if key_pressed[K_e]:                    # если нажал е то начать квест
                            quest_1.set_start(True)
                            player.set_quest_run(True)

                        if quest_1.get_start():

                            quest_1.update(key=key_pressed, player=player, lives=lives, quest_numpad=quest_password_num)
                            screen.blit(quest_1.image, quest_1.rect)

                            screen.blit(quest_password_num.image_1, quest_password_num.rect1)
                            screen.blit(quest_password_num.image_2, quest_password_num.rect2)
                            screen.blit(quest_password_num.image_3, quest_password_num.rect3)
                            screen.blit(quest_password_num.image_4, quest_password_num.rect4)
                            screen.blit(quest_password_num.image_5, quest_password_num.rect5)




            # Инвентарь:
            screen.blit(Ivent_panel.image, Ivent_panel.rect)

            user_ivent.update(key_pressed)
            if user_ivent.check_ivent(key_type='Door_124_key'):
                screen.blit(user_ivent.Door_124_key, user_ivent.Door_124_key_rect)
            if user_ivent.check_ivent(key_type='Door_to_end_quest'):
                screen.blit(user_ivent.Door_to_end_quest, user_ivent.Door_to_end_quest_rect)
            if user_ivent.check_ivent(key_type='Pantry'):
                screen.blit(user_ivent.Pantry, user_ivent.Pantry_rect)
            if user_ivent.check_ivent(key_type='Morgue'):
                screen.blit(user_ivent.Morgue,  user_ivent.Morgue_rect)

            if l == 5 and a <= Shado_bottom:           #Отображение Shado поверх игрока
                screen.blit(shado.image, shado.rect)
                shado.update(key=key_pressed, player = player)


            if map_on:  # Включение карты
                screen.blit(map.image, map.rect)  # Отрисовка карты

            if lives.check_healt() == 0:
                run = False

            replic = check_replic(l)                                             # Проверка есть ли  реплики на данном уровне

            if replic == True:
                replic_pos = check_replic_pos(l)                        # Позиция для запуска диалога
                if l in replic_level and player.check_right() >= replic_pos and player.check_right() <= replic_pos + 150:
                    if (player_replic_ask < repliks[l][0][0] and not repliks[l][1]) \
                            or (repliks[l][2] and player_replic_ask < repliks[l][0][2] + repliks[l][0][0] and not repliks[l][1]):                                      # Не даем игроку ходить
                        player.set_replic(True)
                        screen.blit(Replic_windows.image, Replic_windows.rect)          # Отрисовываем панель диалога игрока
                        Replic_windows.update('Player')
                        text_replic = check_replic_player(player, l, player_replic_ask)

                        text_print_replic = print_effect(text_replic)

                        txt = font.render(text_print_replic, False, [153, 144, 144])          # Отрисовка реплик
                        screen.blit(txt, (15, 900))

                        for event in pygame.event.get():
                            if event.type == KEYDOWN:
                                if event.key == K_RETURN:                                       # Если нажат Enter переходим дальше
                                    player_replic_ask += 1
                                    if player_replic_ask >= repliks[l][0][0] + repliks[l][0][2]:   # Если реплики закончились идем дальше
                                        repliks[l][1] = True
                                        player.set_replic(False)
                                        player_replic_ask = 0

                    else:
                        if not repliks[l][2]:
                            #replic_s = random.randint(1, 2)
                            screen.blit(Replic_windows.image, Replic_windows.rect)       # Отрисовываем панель диалога Shado
                            Replic_windows.update('Shado')
                            text_replic = check_replic_Shado(player, l, shado_replic_ask)

                            # text_style = get_replic_font('shado')                              #Шрифт текста Shado
                            # if replic_s == 1:
                            #     text_style = get_replic_font('shado')
                            # elif replic_s == 2:
                            #     text_style = get_replic_font('angry')

                            text_print_replic = print_effect(text_replic)

                            txt1 = shado_engry_font.render(text_print_replic[0:90], False, [128, 6, 6])             # Отрисовка реплик в зависимости от их длинны
                            txt2 = shado_engry_font.render(text_print_replic[90:180], False, [128, 6, 6])
                            txt3 = shado_engry_font.render(text_print_replic[180:270], False, [128, 6, 6])


                            screen.blit(txt1, (15, 900))
                            screen.blit(txt2, (15, 930))
                            screen.blit(txt3, (15, 960))

                            for event in pygame.event.get():
                                if event.type == KEYDOWN:
                                    if event.key == K_RETURN:
                                        shado_replic_ask += 1
                                        if shado_replic_ask >= repliks[l][0][1]:
                                            shado_replic_ask = 0
                                            repliks[l][2] = True


            pygame.display.flip() # Отрисовка всего на экране
            pygame.display.update()
            clock.tick(FPS) #Контроль скорости игры

# Повтор игры
Game_over = True
while Game_over:
    main()
