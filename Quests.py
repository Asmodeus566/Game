from Game_texture import *
from Game_player import *
from Game_enemy import *
from Check_сollision import *
import pygame

"""

Здесь находится:
1. Класс для первого квеста (Quest_1)
2. Класс для отображения цифр и других изображений для квестов(Quests_number_print)

"""

class Quest_1(pygame.sprite.Sprite):   # Отображение квеста с кодом
    def __init__(self, numberd):
        super(Quest_1, self).__init__()
        self.password_user =                []
        self.password =                     numberd
        self.start_quest =                  False
        self.quest_end =                    False
        self.image =                        pygame.image.load('image/Quests/Quest_1_panel.png')
        self.rect =                         self.image.get_rect()
        self.rect.left, self.rect.bottom =  200, 815

    def update(self, key, player, lives, quest_numpad):
        if self.start_quest:
            self.image =                        pygame.image.load('image/Quests/Quest_1_panel.png')
            self.rect =                         self.image.get_rect()
            self.rect.left, self.rect.bottom =  250, 815

            if len(self.password_user) >= 0:                      # Получение нажатых клавиш и занесение их в список
                if key[K_1]:
                    self.password_user.append("1")
                    quest_numpad.update(self.password_user)
                if key[K_2]:
                    self.password_user.append("2")
                    quest_numpad.update(self.password_user)
                if key[K_3]:
                    self.password_user.append("3")
                    quest_numpad.update(self.password_user)
                if key[K_4]:
                    self.password_user.append("4")
                    quest_numpad.update(self.password_user)
                if key[K_5]:
                    self.password_user.append("5")
                    quest_numpad.update(self.password_user)
                if key[K_6]:
                    self.password_user.append("6")
                    quest_numpad.update(self.password_user)
                if key[K_7]:
                    self.password_user.append("7")
                    quest_numpad.update(self.password_user)
                if key[K_8]:
                    self.password_user.append("8")
                    quest_numpad.update(self.password_user)
                if key[K_9]:
                    self.password_user.append("9")
                    quest_numpad.update(self.password_user)
                if key[K_0]:
                    self.password_user.append("0")
                    quest_numpad.update(self.password_user)
                if key[K_BACKSPACE]:
                    if len(self.password_user) > 0:
                        self.password_user.pop(len(self.password_user) -1)
                        quest_numpad.update(self.password_user)

            if len(self.password_user) < 5 and key[K_RETURN]:       # Если игрок ввеедт код меньше 5 символов то отнять здоровье и прекратить квест
                quest_numpad.update([0,0,0,0,0])
                del self.password_user[0:10]
                lives.healt_minus(50)
                player.set_quest_run(False)
                self.start_quest = False

            elif len(self.password_user) >= 5:                      # Если код введен весь, то проверяем совпадает ли он
                if key[K_RETURN]:
                    self.check_pas = ("".join(self.password_user[0:5]))
                    print(self.password_user)

                    print(self.password_user, '+ ', self.password)

                    if int(self.check_pas) == self.password:
                                                                    # Если совпадает то завершаем квест
                        player.set_quest_run(False)                 # Позвалаям игроку двигаться, так же в основном файле открывается доступ к двери на первом уровне
                        self.start_quest = False
                        self.quest_end = True
                    else:
                                                                    # В противном случае завершаем квест и отнимаем здоровье
                        lives.healt_minus(50)
                        player.set_quest_run(False)
                        self.start_quest = False

    def get_start(self):
        return self.start_quest

    def set_start(self, start):
        self.start_quest = start

    def get_quest_end(self):
        return self.quest_end

    def get_user_password(self):
        return self.password_user

class Quests_number_print(pygame.sprite.Sprite):  # Отображения цифр и т.д для квестов

    def __init__(self):
        super(Quests_number_print, self).__init__()
        self.picture = {0: "image\password\Calculat_0.png", 1: "image\password\Calculat_1.png", 2: "image\password\Calculat_2.png",
                        3: "image\password\Calculat_3.png", 4: "image\password\Calculat_4.png", 5: "image\password\Calculat_5.png",
                        6: "image\password\Calculat_6.png", 7: "image\password\Calculat_7.png", 8: "image\password\Calculat_8.png",
                        9: "image\password\Calculat_9.png"}

        self.image_1 = pygame.image.load(self.picture[0])
        self.image_2 = pygame.image.load(self.picture[0])
        self.image_3 = pygame.image.load(self.picture[0])
        self.image_4 = pygame.image.load(self.picture[0])
        self.image_5 = pygame.image.load(self.picture[0])

        self.rect1 = self.image_1.get_rect()
        self.rect2 = self.image_2.get_rect()
        self.rect3 = self.image_3.get_rect()
        self.rect4 = self.image_4.get_rect()
        self.rect5 = self.image_5.get_rect()

        self.rect1.right, self.rect1.bottom = 300, 508
        self.rect2.left, self.rect2.bottom = self.rect1.right + 4, 508
        self.rect3.left, self.rect3.bottom = self.rect2.right + 4, 508
        self.rect4.left, self.rect4.bottom = self.rect3.right + 4, 508
        self.rect5.left, self.rect5.bottom = self.rect4.right + 4, 508

    def update(self, number):   # Добаить потом quest_number, для указывания номера квеста
        self.quest_number = 1
        self.pasw = [0, 0, 0, 0, 0]
        if self.quest_number == 1:                                  # Первый квест
            self.picture = {0: "image\password\Calculat_0.png", 1: "image\password\Calculat_1.png",
                            2: "image\password\Calculat_2.png",
                            3: "image\password\Calculat_3.png", 4: "image\password\Calculat_4.png",
                            5: "image\password\Calculat_5.png",
                            6: "image\password\Calculat_6.png", 7: "image\password\Calculat_7.png",
                            8: "image\password\Calculat_8.png",
                            9: "image\password\Calculat_9.png"}

            # Просто пиздец надеюсь не запутаюсь в будующе(Отображение цифр на кодовом замке)

            try:
                for i in range(len(number)):
                    self.pasw[i] = int(number[i])
                self.image_1 = pygame.image.load(self.picture[int(self.pasw[0])])
                self.image_2 = pygame.image.load(self.picture[int(self.pasw[1])])
                self.image_3 = pygame.image.load(self.picture[int(self.pasw[2])])
                self.image_4 = pygame.image.load(self.picture[int(self.pasw[3])])
                self.image_5 = pygame.image.load(self.picture[int(self.pasw[4])])
            except IndexError:
                pass


        else:
            pass