import pygame
from Game_player import *
from random import *

"""
В этом файле находятся:
1. Функция выбора фона в зависимости от уровня
2. Показ текста при подходе к двери
3. Определение позиции текста в зависимости от позиции двери
4. Позиция дверей
5. Позиция Квестов
6. Класс здоровья игрока(UserHealts)
7. Класс выносливости игрока(User_Stat)
8. Класс заднего фона (Background)
9. Класс карты (Map)
10.Класс меню (Menu)
11. Класс настроек(Settings)
12. Класс информации(Info)
13. Класс паузы игры(Game_pause)
14. Класс Инвентаря игрока(User_ivent)
14.1 Класс панели для инвентаря(IventPanel)
15. Класс пуль(Pyl)
16. Класс дверей(Door)
17. Класс для отображения кода на пентограмме(PaswordNumber)
18. Класс тображение меток для квестов(Quests)
"""

#Выбор изображения фона
def Photo_load(l, a, a2):
    image = ['image\levels\lvl1.png', 'image\levels\lvl2.png', 'image\levels\lvl3.png', 'image\levels\lvl4.png',
             'image\levels\lvl5.png', 'image\levels\lvl6.png', 'image\levels\lvl7.png', 'image\levels\lvl8.png',
             'image\levels\lvl12.png']

    try:
        im = image[l]
    except:
        im = image[-1]
    return im

# Текст
def text_on(door, door2, level, player):
    text = None
    levels = [0, 8, 9, 10]
    if level in levels:
        if door.check_open_door():
            text = 'E-Войти'
        elif door2.check_open_door():
            text = 'E-Войти'
        if not door.check_quest_end() and player.check_bottom() <= door.check_bottom() + 30 and player.check_left() \
                >= door.check_left() - 20 and player.check_right() <= door.check_right() + 20:
            text = 'Закрыто'

    else:
        text = None

    return text


def unfisiball_wall(l):
    try:
        position = {0: {'bottom': 678, 'left': 1045, 'right': 1280}, 1: {'bottom': 655, 'left': 0, 'right': 52},
                    4: {'bottom': 675, 'left': 0, 'right': 40}, 5: {'bottom':710, 'right': 700, 'left': 345}}

        return position[l]
    except KeyError:
        pass

# Позиция текста
def text_pos(door, door2):
    pos_x = None
    pos_y = None

    door_left = door.check_left()
    door_top =  door.check_top()

    if door.check_open_door() or not door.check_open_door():
        pos_x = door_left
        pos_y = door_top - 30
    else:
        pos_x, pos_y = None, None

    return pos_x, pos_y

# Установление позиции двери
def door_position(level):
    dor_pos = {0: [690, 620], 8: [300, 620], 9: [400, 620], 10: [500, 620]}

    return dor_pos[level]

def quest_pos(level):
    quest_position = {0: [630, 550], 3: [300, 550], 5: [300, 550], 8: [300, 550],10: [300, 550], 13: [300, 550], 6: [200, 550]}

    return quest_position[level]


class UserHealts(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.len =                          [150, 15]
        self.kol =                          0
        self.image =                        pygame.image.load("image/sprite/player/health_panel.png")
        self.rect =                         self.image.get_rect()
        self.rect.left, self.rect.bottom =  135, 137

    def healts_update(self, lives):
        self.n = lives
        if self.n > self.kol:
            x = self.len[0] - 6
            y = self.len[1]
            self.len = [x, y]
            self.kol += 1


        self.image =                        pygame.image.load("image/sprite/player/health_panel.png")
        self.image =                        pygame.transform.scale(self.image, self.len)
        self.rect =                         self.image.get_rect()
        self.rect.left, self.rect.bottom =  135, 125


        if self.n == 25:
            return 1
        else:
            return 0
    def healt_minus(self, kol):
        if self.len[0] >0:
            self.len[0] -= kol

    def check_healt(self):
        return self.len[0]

class User_Stat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.full_stat_use =                False
        self.len =                          [150, 15]
        self.n, self.n2 =                   0, 0
        self.run_count, self.run2_count =   0, 0
        self.image =                        pygame.image.load("image/sprite/player/stat_panel.png")
        self.rect =                         self.image.get_rect()
        self.rect.left, self.rect.bottom =  135, 155

    def update(self, run):
        if run and self.len[0] >= 2:
            self.len[0] -=  1
            self.image =    pygame.image.load("image/sprite/player/stat_panel.png")
            self.image =    pygame.transform.scale(self.image, self.len)

        elif run and self.len[0] <= 1:
            self.full_stat_use =    True
            self.len[0] =           1

        elif not run and self.len[0] < 150:
            self.len[0] +=  1
            self.image =    pygame.image.load("image/sprite/player/stat_panel.png")
            self.image =    pygame.transform.scale(self.image, self.len)
            if self.len[0] > 50:
                self.full_stat_use = False

        else:
            self.image = pygame.image.load("image/sprite/player/stat_panel.png")
            self.image = pygame.transform.scale(self.image, self.len)

    def check_stat(self):
        return self.len[0]

    def check_full_stat_use(self):
        return self.full_stat_use


# Изображения заднего фона
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image =                    pygame.image.load(image_file).convert_alpha()
        self.rect =                     self.image.get_rect()
        self.rect.left, self.rect.top = location

#Карта игрока:
class Map():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =                    pygame.image.load('image\map.png').convert_alpha()
        self.rect =                     self.image.get_rect()
        self.rect.left, self.rect.top = [0, 0]

# Текстура меню
class Menu():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =                    pygame.image.load('image\menu.png').convert_alpha()
        self.rect =                     self.image.get_rect()
        self.rect.left, self.rect.top = [0,0]

# НАстройки
class Settings():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image =                    pygame.image.load('image\levels\lvl1.jpg').convert_alpha()
        self.rect =                     self.image.get_rect()
        self.rect.left, self.rect.top = [0, 0]
# Информация и помощь
class Info():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image =                    pygame.image.load('image\Info.png').convert_alpha()
        self.rect =                     self.image.get_rect()
        self.rect.left, self.rect.top = [0, 0]

#Поуза
class Game_pause():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =                        pygame.image.load('image\map.png').convert_alpha()
        self.rect =                         self.image.get_rect()
        self.rect.left, self.rect.top =     [0, 0]

# Инвентарь

class IventPanel():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =                        pygame.image.load('image\ivent_panel.png').convert_alpha()
        self.rect =                         self.image.get_rect()
        self.rect.right, self.rect.top =    [1280, 100]

class User_ivent():
    def __init__(self):
        self.have_key = {"Door_124_key" : True, "Door_to_end_quest" : True, "Pantry" : False, "Morgue" : False}
        self.l = [12, 13]
        self.random_level = {'Door_124_key': 0, 'Door_to and_quest': 12, "Pantry": choice(self.l), 'Morgue': 14}
        # Изображение кдючей и их позиция
        self.image_item = {
            "Door_124_key" : ['image/Keys/Door_124_key.png', [1118,150]],
            "Door_to_end_quest" :  ['', [1167,150]],
            "Pantry" :  ['', [1218,150]],
            "Morgue" :  ['', [1267,150]]
        }

        self.Door_124_key =                                             pygame.Surface((35, 45))
        self.Door_124_key.fill((255,0,0))
        self.Door_124_key_rect =                                        self.Door_124_key.get_rect()
        self.Door_124_key_rect.right, self.Door_124_key_rect.bottom =   1120, 150

        self.Door_to_end_quest =                                                pygame.Surface((35, 45))
        self.Door_to_end_quest.fill((0, 255, 0))
        self.Door_to_end_quest_rect =                                           self.Door_to_end_quest.get_rect()
        self.Door_to_end_quest_rect.right, self.Door_to_end_quest_rect.bottom = 1170, 150

        self.Pantry =                                       pygame.Surface((35, 45))
        self.Pantry.fill((0, 0, 255))
        self.Pantry_rect =                                  self.Pantry.get_rect()
        self.Pantry_rect.right, self.Pantry_rect.bottom =   1220, 150

        self.Morgue =                                       pygame.Surface((35, 45))
        self.Morgue.fill((255, 255, 0))
        self.Morgue_rect =                                  self.Morgue.get_rect()
        self.Morgue_rect.right, self.Morgue_rect.bottom =   1270, 150


    def update(self, key):


        if self.have_key["Door_124_key"] ==                                 True:
            self.Door_124_key =                                             pygame.image.load(self.image_item['Door_124_key'][0])
            self.Door_124_key_rect.right, self.Door_124_key_rect.bottom =   1120, 150

        # Будущие ключи \:
        # if self.have_key["Door_to_end_quest"] == True:
        #     self.Door_to_end_quest = pygame.image.load(self.image_item['Door_to_end_quest'][0])
        #     self.Door_to_end_quest_rect.right, self.Door_to_end_quest_rect.bottom = 1170, 150
        #
        # if self.have_key['Pantry'] == True:
        #     self.Pantry = pygame.image.load(self.image_item['Patry'][0])
        #     self.Pantry_rect.right, self.Pantry_rect.bottom = 1220, 150
        #
        # if self.have_key["Morgue"] == True:
        #     self.Morgue = pygame.image.load(self.image_item['Morgue'][0])
        #     self.Morgue_rect.right, self.Morgue_rect.bottom = 1270, 150


    def set_true_or_false(self, name, pos):
        self.have_key[name] = pos

    def check_ivent(self, key_type):
        return self.have_key[key_type]

    def check_ivent_all(self):
        return self.have_key

# Дверь
class Door(pygame.sprite.Sprite):
    def __init__(self,):
        super(Door, self).__init__()
        self.quest_end                      = False
        self.door_open                      = False
        self.dor_pos                        = [690, 620]
        self.door_left                      = self.dor_pos[0]
        self.door_bottom                    = self.dor_pos[1]
        self.open_door                      = 'image\open__door.png'
        self.close_door                     = 'image\close_door.png'
        self.image                          = pygame.image.load(self.close_door)
        self.rect                           = self.image.get_rect()
        self.rect.bottom, self.rect.left    = self.door_bottom, self.door_left

    # Update
    def update(self, pos, level, player, quest):
        player_left         = player.check_left()
        player_right        = player.check_right()
        player_bottom       = player.check_bottom()
        self.dor_pos        = pos

        if quest.get_quest_end():
            self.quest_end = True

        if pos[0] != None and pos[1] != None:
            if player_bottom <= self.rect.bottom and (player_right >= self.rect.left or player_left >= self.rect.left) and (player_right <= self.rect.right or player_left <= self.rect.right) and quest.get_quest_end():
                self.image =                        pygame.image.load(self.open_door)
                self.rect.bottom, self.rect.left =  pos[1], pos[0]
                self.door_open =                    True
            else:
                self.image =                        pygame.image.load(self.close_door)
                self.rect.bottom, self.rect.left =  pos[1], pos[0]
                self.door_open =                    False

    def check_open_door(self):
        return self.door_open

    def check_left(self):
        return self.rect.left

    def check_right(self):
        return self.rect.right

    def check_top(self):
        return self.rect.top

    def check_bottom(self):
        return self.rect.bottom

    def check_quest_end(self):
        return self.quest_end



class PasswordNumber(pygame.sprite.Sprite):  # Отображения кода около пентограммы

    def __init__(self, number):
        super(PasswordNumber, self).__init__()
        self.num_all = number
        self.picture = {0: "image\password\(0.png", 1: "image\password\(1.png", 2: "image\password\(2.png",
                        3: "image\password\(3.png", 4: "image\password\(4.png", 5: "image\password\(5.png",
                        6: "image\password\(6.png", 7: "image\password\(7.png", 8: "image\password\(8.png",
                        9: "image\password\(9.png"}
        self.num1 = number[0]
        self.num2 = number[1]
        self.num3 = number[2]
        self.num4 = number[3]
        self.num5 = number[4]
        # Загрузка изображений для цифр
        self.image1 = pygame.image.load(self.picture[int(self.num1)])
        self.image2 = pygame.image.load(self.picture[int(self.num2)])
        self.image3 = pygame.image.load(self.picture[int(self.num3)])
        self.image4 = pygame.image.load(self.picture[int(self.num4)])
        self.image5 = pygame.image.load(self.picture[int(self.num5)])
        # Игнорирование заднего фона
        self.image1.set_colorkey((0, 0, 0))
        self.image2.set_colorkey((0, 0, 0))
        self.image3.set_colorkey((0, 0, 0))
        self.image4.set_colorkey((0, 0, 0))
        self.image5.set_colorkey((0, 0, 0))
        # Получение позиции
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect3 = self.image3.get_rect()
        self.rect4 = self.image4.get_rect()
        self.rect5 = self.image5.get_rect()
        # Настройки позиции
        self.rect1.right, self.rect1.bottom = 527, 394
        self.rect2.left, self.rect2.bottom  = 612, 293
        self.rect3.left, self.rect3.bottom  = 755, 391
        self.rect4.left, self.rect4.bottom  = 698, 564
        self.rect5.right, self.rect5.bottom = 585, 570


class Quests(pygame.sprite.Sprite):  # Отображение метки квеста с вводом кода

    def __init__(self):
        super(Quests, self).__init__()
        # 50, 70
        #Метки квеста. Сейчас одинаковые для тестирование.
        self.quest_image =                  {0: 'image/Quests/Panel.png', 3: 'image/Quests/Panel.png', 6: 'image/Quests/Panel.png', 5: 'image/Quests/Panel.png'}
        self.quest_start =                  False
        self.pos =                          [300, 550]
        self.image =                        pygame.image.load(self.quest_image[0])
        self.rect =                         self.image.get_rect()
        self.rect.left, self.rect.bottom =  self.pos[0], self.pos[1]

    def update(self, position, l):                                      # Обноление вида меток в зависимости от уровня

        self.pos = position                                             # Список с позицией квеста
        self.image = pygame.image.load(self.quest_image[l])             # Установка изображения из списка по номеру уровню
        self.rect.left, self.rect.bottom = self.pos[0], self.pos[1]

    def check_quest(self):                                              # Функция проверки начат ли квест
        return self.quest_start

    def set_quest(self, status):
        self.quest_start = status

    def check_top(self):
        return self.rect.top



