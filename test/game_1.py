import numpy as np
import pygame, sys
from settings import Settings

# Цвет основного экрана
bg_color = (50, 50, 50)
window = pygame.display.set_mode((400, 400))
screen = pygame.Surface((400, 400))

def run_game():
    box1 = Sprite(0, 0, "box_1.png")
    box2 = Sprite(50, 0, "box_2.png")
    box3 = Sprite(100, 0, "box_3.png")
    box4 = Sprite(150, 0, "box_4.png")

    # Шрифты
    pygame.font.init()

    # Создадим меню
    punkts = [(120, 140, u"Играть", (250, 250, 30), (250, 30, 250), 0),
              (130, 210, u"Выход", (250, 250, 30), (250, 30, 250), 1)]
    game = Menu(punkts)
    game.menu()

    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Манчкин Квест")

    # Основной цикл программы
    done = True
    while done:
        # Если сработало событие закрытие окна то done = True
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
        # Перерисовка экрана
        screen.fill(ai_settings.bg_color)
        # Отображаем
        box1.render()
        box2.render()
        box3.render()
        box4.render()


        #Основной экран
        window.blit(screen, (0, 0))
        pygame.display.flip()

def main(x, y):
    b = np.array([[0, 1, 2, 3, 4],
                 [10, 11, 12, 13, 14],
                 [20, 21, 22, 23, 24],
                 [30, 31, 32, 33, 34],
                 [40, 41, 42, 43, 44]])

    return b[x][y]


class Sprite:
    def __init__(self,xpos,ypos,filename):
        self.x=xpos
        self.y=ypos
        self.bitmap=pygame.image.load(filename)
        #Какой цвет у изображения сделать прозрачным (если фон черный)
        self.bitmap.set_colorkey((0,0,0))
    # Отображает объект на игровой экран
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))


class Menu:
    def __init__(self, punkts=[120, 140, u'Punkt', (250, 250, 30), (250, 30, 250)]):
        self.punkts = punkts
    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self):
        done = True
        font_menu = pygame.font.Font("fonts/10672.ttf", 50)
        punkt = 0
        while done:
            # Цвет основного экрана
            screen.fill(bg_color)
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.type == pygame.K_ESCAPE:
                        sys.exit()
                    # Навигация в меню с помощью клавиш
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts)-1:
                            punkt += 1
                    #Навигация в меню с помощью мыши
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()

            # Основной экран
            window.blit(screen, (0, 0))
            # Отображение последнего прорисованного экрана.
            pygame.display.flip()





run_game()