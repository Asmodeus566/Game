import time

import pygame
from pygame.locals import *
from Game_texture import *
"""
Здесь находится класс Игрока и также переход между уровнями через двери(в калссе игрока)
Ввод имени игрока
"""

"""
Добавить блокировку движения игрока во время квеста с Shado
"""


SCREEN_WIDTH =  1280
SCREEN_HEIGHT = 1024
#Ограничения хождения игрока вверх и вниз:
TOP_USER_WALK = 618  # Верхнее ограничение
MIN_USER_WALK = 824 # Нижнее ограничение


class Player(pygame.sprite.Sprite):

    def __init__(self, n):
        super(Player, self).__init__()

        self.quest_run     = False
        self.key_press     = False
        self.run           = False
        self.walk          = 8
        self.dead          = 0
        self.animCount     = 0
        self.animIdleCount = 0
        self.image_player  = "image/sprite/player/player_idle1.png"
        self.LEVEL         = n
        self.image         = pygame.image.load(self.image_player).convert_alpha()
        self.rect          = self.image.get_rect( center = (40 , 700))
        self.replic        = False
        self.pause         = False
        # Двидение игрока:

    def update(self, key, stat, stat_use, door, quest, check_key, shado, wall):
        self.check_key = check_key
        # 6
        #Анимация
        self.user_anim = ['image\sprite\player\Animation\walk1.png', 'image\sprite\player\Animation\walk2.png',
                          'image\sprite\player\Animation\walk3.png', 'image\sprite\player\Animation\walk4.png',
                          'image\sprite\player\Animation\walk5.png', 'image\sprite\player\Animation\walk6.png',
                          'image\sprite\player\Animation\walk7.png', 'image\sprite\player\Animation\walk8.png',
                          'image\sprite\player\Animation\walk9.png', 'image\sprite\player\Animation\walk10.png',
                          'image\sprite\player\Animation\walk1.png', 'image\sprite\player\Animation\walk2.png',
                          'image\sprite\player\Animation\walk3.png', 'image\sprite\player\Animation\walk4.png',
                          'image\sprite\player\Animation\walk5.png', 'image\sprite\player\Animation\walk6.png',
                          'image\sprite\player\Animation\walk7.png', 'image\sprite\player\Animation\walk8.png',
                          'image\sprite\player\Animation\walk9.png', 'image\sprite\player\Animation\walk10.png',
                          'image\sprite\player\Animation\walk1.png', 'image\sprite\player\Animation\walk2.png',
                          'image\sprite\player\Animation\walk3.png', 'image\sprite\player\Animation\walk4.png',
                          'image\sprite\player\Animation\walk5.png', 'image\sprite\player\Animation\walk6.png',
                          'image\sprite\player\Animation\walk7.png', 'image\sprite\player\Animation\walk8.png',
                          'image\sprite\player\Animation\walk9.png', 'image\sprite\player\Animation\walk10.png'
                          ]

        self.idleAnimation = ["image/sprite/player/player_idle1.png", "image/sprite/player/player_idle2.png",
                              "image/sprite/player/player_idle1.png", "image/sprite/player/player_idle2.png",
                              "image/sprite/player/player_idle1.png", "image/sprite/player/player_idle2.png"]

        if not self.quest_run and not self.replic and not self.pause:   # Позволяем игроку двигаться если он не в квесте
            if key[K_UP] or key[K_w]: #Вверх
                self.rect.move_ip(0, -self.walk)
                self.key_press = True
            if key[K_DOWN] or key[K_s]: #Вниз
                self.rect.move_ip(0, self.walk)
                self.key_press = True
            if key[K_LEFT] or key[K_a]: #Влево
                self.rect.move_ip(-self.walk, 0)
                self.key_press = True
            if key[K_RIGHT] or key[K_d]: # Вправо
                self.rect.move_ip(self.walk, 0)
                self.key_press = True

            if key[K_LSHIFT] and stat and not stat_use:
                self.key_press = True
                self.walk = 70
                self.run = True
            else:
                self.walk = 8
                self.run = False


        if key[K_RIGHT] or key[K_d]:    #Контроль анимации
            self.animIdleCount = 0
            if self.animCount >= 60:
                self.animCount = 0

            elif self.animCount < 60:
                self.image = pygame.image.load(self.user_anim[self.animCount // 2])
                self.animCount += 1

        elif key[K_DOWN] or key[K_s]:
            self.animIdleCount = 0
            if self.animCount >= 60:
                self.animCount = 0

            elif self.animCount < 60:
                self.image = pygame.image.load(self.user_anim[self.animCount // 2])
                self.animCount += 1

        elif key[K_LEFT] or key[K_a]:
            self.animIdleCount = 0
            if self.animCount >= 60:
                self.animCount = 0

            elif self.animCount < 60:
                self.image = pygame.image.load(self.user_anim[self.animCount // 2])
                self.image = pygame.transform.flip(self.image, True, False)
                self.animCount += 1
        else:
            self.animCount = 0
            if self.animIdleCount >= 60:
                self.animIdleCount = 0
            elif self.animIdleCount <= 60:
                self.image = pygame.image.load(self.idleAnimation[self.animIdleCount// 10])
                self.animIdleCount += 1


        # Удержание пользователя в нужных границах:
        if self.rect.bottom >= MIN_USER_WALK:
            self.rect.bottom = MIN_USER_WALK
        if self.rect.bottom <= TOP_USER_WALK:
            self.rect.bottom = TOP_USER_WALK


        """
        Ограничение хождения игрока сквозь предметы
        """
        self.wall = wall
        try:
            if self.rect.bottom <= self.wall['bottom'] and ((self.rect.right >= self.wall['left'] and self.rect.right <= self.wall['right']) \
                    or (self.rect.left <= self.wall['right'] and self.rect.left >= self.wall['left'])):
                if self.rect.right >= self.wall['left'] and self.rect.left < self.wall['left'] - 40 and self.rect.bottom <= self.wall['bottom']:
                    self.rect.right = self.wall['left']
                elif self.rect.left <= self.wall['right'] and self.rect.right > self.wall['right'] + 40 and self.rect.bottom <= self.wall['bottom']:
                    self.rect.left = self.wall['right']
                else:
                    self.rect.bottom = self.wall['bottom']
        except TypeError:
            pass

        # Если квест с Shado не закончен, не давать игроку идти дальше чем Shado
        if self.LEVEL == 5 and not shado.check_shado_quest_end() and self.rect.right >= shado.check_right() - 15:
            self.rect.right = shado.check_right() - 15

        # Переключение пользщователя на новый уровень

        if self.rect.right >= SCREEN_WIDTH and (self.LEVEL < 5 or self.LEVEL > 5):
            self.rect.left = 40                             # Телепортируем пользователя в позицию по X = 40
            self.LEVEL += 1                                 # Прибавляем уровень

        elif self.rect.right >= SCREEN_WIDTH and self.LEVEL == 5:
            self.rect.right = 1280

        #Если пользователь на первом уровне не давать ему идти назад
        if self.rect.left < 0 and (self.LEVEL == 0 or self.LEVEL == 6):
            self.rect.left = 0
        # Если пользователь не на 1 уровне, то позвольть ему вернуться
        if self.rect.left < 0 and (self.LEVEL != 0 or self.LEVEL != 6):
            self.LEVEL -= 1 # Отнимаем один уровень
            self.rect.right = SCREEN_WIDTH - 20 #Телепортируем пользователя в позицию SCREEN_WIDTH - 20 по X при новом уровне

        self.check_level_door(key, door, quest, self.check_key)




    # Проверка нижнего положения игрока игрока
    def check_bottom(self):
        return self.rect.bottom

    # Проверка правого положения игрока игрока
    def check_right(self):
        return self.rect.right

    # Проверка левого положения игрока игрока
    def check_left(self):
        return self.rect.left

    # Проверка верхнего положения игрока игрока
    def check_top(self):
        return self.rect.top

    def check_top_right(self):
        return self.rect.topright

    def check_top_left(self):
        return self.rect.topleft

    def check_bottom_left(self):
        return self.rect.bottomleft

    def check_bottom_right(self):
        return self.rect.bottomright

    # Проверка уровня игрока
    def check_level(self):
        return self.LEVEL

    def check_dead(self):
        return  self.dead

    def check_run(self):
        return self.run

    def set_quest_run(self, status):
        self.quest_run = status

    def set_replic(self, pos):
        self.replic = pos

    def set_pause(self, turn):
        self.pause = turn

    def get_pause(self):
        return self.pause

    def set_color(self, Color1):
        self.color1 = Color1



    def check_level_door(self, key, door, quest, check_key):                  # перемещения между уровнями через двери

        if self.LEVEL == 1:
            if not check_key["Door_124_key"]:                                  # если нет ключа не пускаем игрока через дверь
                if self.rect.bottom >= 618 and self.rect.bottom <= 824:
                    if self.rect.right > 980:
                        if self.rect.right >= self.rect.bottom + 360:
                            self.rect.right = self.rect.bottom + 360

            if check_key["Door_124_key"]:                                      # если есть ключа то пускаем игрока через дверь
                if self.rect.bottom >= 618 and self.rect.bottom <= 824:
                    if self.rect.right > 980:
                        if self.rect.right >= self.rect.bottom + 360:
                            self.rect.right = self.rect.bottom + 360
                            if self.rect.bottom >658 and self.rect.bottom < 758 and key[K_e]:
                                self.LEVEL += 1
                                self.rect.left = 40

        elif self.LEVEL == 4:                                                  # Аналогично с первой
            if not check_key["Door_to_end_quest"]:
                if self.rect.bottom >= 618 and self.rect.bottom <= 824:
                    if self.rect.right > 980:
                        if self.rect.right >= self.rect.bottom + 360:
                            self.rect.right = self.rect.bottom + 360

            if check_key["Door_to_end_quest"]:                                                        # Аналогично с первой
                if self.rect.bottom >= 618 and self.rect.bottom <= 824:
                    if self.rect.right > 980:
                        if self.rect.right >= self.rect.bottom + 360:
                            self.rect.right = self.rect.bottom + 360
                            if self.rect.bottom > 658 and self.rect.bottom < 758 and key[K_e]:
                                self.LEVEL += 1
                                self.rect.left = 40

        elif self.LEVEL == 0 and quest.get_quest_end():                         # Пустить игока в кабинет если он правильно ввеел код
            if self.rect.bottom <= door.check_bottom() + 10 and (self.rect.right >= door.check_left() and self.rect.right <= door.check_right()) or (self.rect.left <= door.check_right() and self.rect.right >= door.check_left()):
                if key[K_e]:
                    self.rect.left = 40
                    self.rect.bottom = 820
                    self.LEVEL = 6

        elif self.LEVEL == 6 and self.rect.bottom >= MIN_USER_WALK -5 and self.rect.left <= 100:
            if key[K_e]:
                self.LEVEL = 0
                self.rect.right, self.rect.bottom = door.check_left() - 10, door.check_bottom() + 5

        else:
            pass

