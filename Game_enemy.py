from Check_сollision import player_pursuit
import pygame
import random
from pygame.locals import *
pygame.init()
from sys import *
"""
Здесь находится:
1. Класс противника(Enemy)
2. Класс главного врага (Shado)
"""

class Enemy(pygame.sprite.Sprite):   # Противник
    def __init__(self):
        super(Enemy, self).__init__()
        self.TOP_USER_WALK = 618  # Верхнее ограничение
        self.MIN_USER_WALK = 824  # Нижнее ограничение

        self.pos_x                          = random.randint(640, 1150)
        self.pos_y                          = random.randint(618, 800)
        self.image                          = pygame.image.load('image/sprite/enemy/enemy.png')
        self.rect                           = self.image.get_rect()
        self.rect.left, self.rect.bottom    = self.pos_x, self.pos_y
        self.died                           = False

    def update(self, player, enemy):
        self.cor        = player_pursuit(player, enemy)
        self.step_x     = self.cor[0]
        self.step_y     = self.cor[1]

        # if not player.get_pause():
        #     self.rect.move_ip(self.step_x, self.step_y)

        self.rect.move_ip(0, 0)

        if self.rect.bottom >= self.MIN_USER_WALK:
            self.rect.bottom = self.MIN_USER_WALK
        if self.rect.bottom <= self.TOP_USER_WALK:
            self.rect.bottom = self.rect.bottom

        if player.check_level() == 0 or player.check_level() == 5:
            self.died = False
        else:
            self.died = True


    def check_top(self):
        return self.rect.top

    def check_left(self):
        return self.rect.left

    def check_right(self):
        return self.rect.right

    def check_bottom(self):
        return self.rect.bottom

    def set_bottom(self, pos):
        self.rect.bottom = pos

    def check_top_right(self):
        return self.rect.topright

    def check_top_left(self):
        return self.rect.topleft

    def check_bottom_left(self):
        return self.rect.bottomleft

    def check_bottom_right(self):
        return self.rect.bottomright

    def kill_enemy(self):
        self.kill()

    def check_died(self):
        return self.died

    def set_dead(self, pos):
        self.died = pos

class Shado(pygame.sprite.Sprite):                     # главный "злодей"
    def __init__(self):
        super(Shado, self).__init__()
                                                        # Файлы для обычной онамации спокойствия
        self.idle = ["image/sprite/Shado/idle1.png", "image/sprite/Shado/idle2.png", "image/sprite/Shado/idle3.png",
                     "image/sprite/Shado/idle1.png", "image/sprite/Shado/idle2.png", "image/sprite/Shado/idle3.png"]
                                                        # Файлы для анимации смерти
        self.death = []
                                                        # Файлы для анимации стрельбы
        self.shot = ["image/sprite/Shado/shot/shot2.png", "image/sprite/Shado/shot/shot3.png", "image/sprite/Shado/shot/shot4.png",
                     "image/sprite/Shado/shot/shot5.png", "image/sprite/Shado/shot/shot6.png", "image/sprite/Shado/shot/shot7.png",
                     "image/sprite/Shado/shot/shot12.png", "image/sprite/Shado/shot/shot13.png", "image/sprite/Shado/shot/shot14.png",
                     "image/sprite/Shado/shot/shot15.png", "image/sprite/Shado/shot/shot16.png", "image/sprite/Shado/shot/shot17.png",
                     "image/sprite/Shado/shot/shot18.png", "image/sprite/Shado/shot/shot19.png", "image/sprite/Shado/shot/shot20.png",

                     "image/sprite/Shado/shot/shot2.png", "image/sprite/Shado/shot/shot3.png", "image/sprite/Shado/shot/shot4.png",
                     "image/sprite/Shado/shot/shot5.png", "image/sprite/Shado/shot/shot6.png", "image/sprite/Shado/shot/shot7.png",
                     "image/sprite/Shado/shot/shot12.png", "image/sprite/Shado/shot/shot13.png", "image/sprite/Shado/shot/shot14.png",
                     "image/sprite/Shado/shot/shot15.png", "image/sprite/Shado/shot/shot16.png", "image/sprite/Shado/shot/shot17.png",
                     "image/sprite/Shado/shot/shot18.png", "image/sprite/Shado/shot/shot19.png", "image/sprite/Shado/shot/shot20.png",

                     "image/sprite/Shado/shot/shot2.png", "image/sprite/Shado/shot/shot3.png", "image/sprite/Shado/shot/shot4.png",
                     "image/sprite/Shado/shot/shot5.png", "image/sprite/Shado/shot/shot6.png", "image/sprite/Shado/shot/shot7.png",
                     "image/sprite/Shado/shot/shot12.png", "image/sprite/Shado/shot/shot13.png", "image/sprite/Shado/shot/shot14.png",
                     "image/sprite/Shado/shot/shot15.png", "image/sprite/Shado/shot/shot16.png", "image/sprite/Shado/shot/shot17.png",
                     "image/sprite/Shado/shot/shot18.png", "image/sprite/Shado/shot/shot19.png", "image/sprite/Shado/shot/shot20.png",

                     "image/sprite/Shado/shot/shot2.png", "image/sprite/Shado/shot/shot3.png",   "image/sprite/Shado/shot/shot4.png",
                     "image/sprite/Shado/shot/shot5.png", "image/sprite/Shado/shot/shot6.png",   "image/sprite/Shado/shot/shot7.png",
                     "image/sprite/Shado/shot/shot12.png", "image/sprite/Shado/shot/shot13.png", "image/sprite/Shado/shot/shot14.png",
                     "image/sprite/Shado/shot/shot15.png", "image/sprite/Shado/shot/shot16.png", "image/sprite/Shado/shot/shot17.png",
                     "image/sprite/Shado/shot/shot18.png", "image/sprite/Shado/shot/shot19.png", "image/sprite/Shado/shot/shot20.png",

                     ]
                                                        # Файлы для анимации длинной руки
        self.long_punch = ["image/sprite/Shado/long_punch/long_punch1.png", "image/sprite/Shado/long_punch/long_punch2.png",
                           "image/sprite/Shado/long_punch/long_punch3.png", "image/sprite/Shado/long_punch/long_punch4.png",
                           "image/sprite/Shado/long_punch/long_punch1.png", "image/sprite/Shado/long_punch/long_punch2.png",
                           "image/sprite/Shado/long_punch/long_punch3.png", "image/sprite/Shado/long_punch/long_punch4.png",
                           "image/sprite/Shado/long_punch/long_punch4.png", "image/sprite/Shado/long_punch/long_punch4.png",
                           ]
                                                        # Счетчик анимации
        self.animCount      = 0
        self.animLongCount  = 0
        self.animShotCount  = 0
                                                        # Контроль стрельбы и длинной руки
        self.Shado_shot = False
        self.Shado_long = False

        self.Shado_quest_end = False

        self.image =                        pygame.image.load(self.idle[0])
        self.rect =                         self.image.get_rect()
        self.rect.right, self.rect.bottom = 810, 700

    def update(self, key, player):

        """
        Добавить блокировку движения игрока во время квеста с Shado
        """

        try:
            if key[K_z]:
                self.Shado_long = True
                player.set_quest_run(True)
                if self.animLongCount >= 60:
                    self.animLongCount = 0

                if self.animLongCount < 60:
                    self.image  = pygame.image.load(self.long_punch[self.animLongCount // 6])
                    self.rect   = self.image.get_rect()
                    self.rect.right, self.rect.bottom = 810, 700

                    self.animLongCount  += 1
                    self.animCount      = 0
                    self.animShotCount  = 0


            elif key[K_x]:
                self.Shado_shot = True
                player.set_quest_run(True)
                if self.animShotCount >=60:
                    self.animShotCount = 0

                if self.animShotCount < 60:
                    self.image =                        pygame.image.load(self.shot[self.animShotCount // 1])
                    self.rect =                         self.image.get_rect()
                    self.rect.right, self.rect.bottom = 810, 700

                    self.animLongCount  = 0
                    self.animCount      = 0
                    self.animShotCount  += 1

            else:
                player.set_quest_run(False)
                if self.animCount >= 60:
                    self.animCount = 0

                elif self.animCount < 60:
                    self.image = pygame.image.load(self.idle[self.animCount // 10])
                    self.rect = self.image.get_rect()
                    self.rect.right, self.rect.bottom = 810, 700

                    self.animCount      += 1
                    self.animLongCount  = 0
                    self.animShotCount  = 0

        except FileNotFoundError:
            print("Ошибка загрузки изображения")


    def check_bottom(self):
        return self.rect.bottom
    
    def check_left(self):
        return self.rect.left
    
    def check_right(self):
        return self.rect.right
    
    def check_top(self):
        return self.rect.top

    def check_shot(self):
        return self.Shado_shot

    def check_long_punch(self):
        return self.Shado_long

    def check_shado_quest_end(self):
        return self.Shado_quest_end

    def set_shado_quest_end(self, set):
        self.Shado_quest_end = set


