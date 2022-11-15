import pygame.sprite
from pygame import *
pygame.init()
pygame.font.init()
import time

"""
Здесь находятся классы для диалог
1. class Replic_window отображающий иконку диалога
2. class Game_replic отвекчающий за реплики P.s удален из-за ненадобности
"""

class Replic_window(pygame.sprite.Sprite):

    def __init__(self):
        super(Replic_window, self).__init__()
        self.image =                        pygame.image.load("image/Player_ask_panel.png")
        self.rect =                         self.image.get_rect()
        self.rect.left, self.rect.bottom =  0, 1000

    def update(self, sprite):
        if sprite == "Player":                              # Загрузка изображения реплики игрока
            self.image = pygame.image.load("image/Player_ask_panel.png")
        if sprite == "Shado":                               # Загрузка изображения реплики Shado
            self.image = pygame.image.load("image/Shado_ask_panel.png")

def get_replic_font(status):
    if status == "player":
        return pygame.font.Font('font/Manga.ttf', 30)
    elif status == "angry":
        return pygame.font.Font('font/SehnsuchtFont.ttf', 20)
    elif status == 'shado':
        return pygame.font.Font('font/Blaze.ttf', 20)


def check_replic(l):
    replic = [0, 1, 2, 5, 12]


    if l in replic:
        return True
    else:
        return False

def check_replic_pos(l):
    try:

        pos = {0: 500, 1: 900,  2: 200, 5: 100, 12: 200}
        return pos[l]
    except KeyError:
        pass

    except IndexError as e:
        print(e)

count   = 0
count2  = 0
txt     = None

def print_effect(text):
    global count, txt, count2
    lenght = len(text)

    if count < lenght and txt != text:
        count   += 2
        txt     = text[0:count]
        return text[0:count]

    else:
        count = 0
        return text[0:]



def check_replic_player(player, l, replic_numb):
    replicNum = {0: 3, 1: 2 ,2: 1, 5: 3, 12: 1}

    replic = {0: [500, False, "Как я здесь оказался?", '???', "Серьезно, что за шутки?"],
              1: [900, False, "Боюсь представить что зо этой дверью", "Говорит что-то что меня похитило, и почему я вообще тебя слышу?"],
              2: [200, False, "Хм... это похоже на какой то код"],
              5: [100, False, "...", "...", ".."],
              12: [200, False, "..."]}

    if replic_numb < replicNum[l]:
        if player.check_right() >= replic[l][0] and not replic[l][1]:
            return replic[l][2+replic_numb]



def check_replic_Shado(player, l, replic_numb):

    replicNum = {0: 3, 1: 2, 2: 2, 5: 6, 12: 2}

    replic = {0: [500, False, "Это я привел тебя сюда...", 'Пройди мои испытания чтобы выбраться от сюда живым...', "Это будет не легко. Я буду всячески тебе мешать"],
              1: [900, False, "Не бойся, за этой дверью ничего страшного нет", "Я же не псих какой то"],
              2: [200, False, "Да ты оказывается Шерлок", "Будь осторожен, у тебя всего 3 попытки ввести пароль потом... СМЕРТЬ"],
              5: [100, False, "...", "///", '///', "...", ",,,", "..."],
              12: [200, False, "...", '...']}
    if replic_numb < replicNum[l]:
        if player.check_right() >= replic[l][0] and not replic[l][1]:
            return replic[l][2 + replic_numb]

