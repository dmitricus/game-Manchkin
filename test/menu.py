import pygame, sys
from settings import Settings

ai_settings = Settings()

class Menu():
    def __init__(self, punkts=[120, 140, u'Punkt', (250, 250, 30), (250, 30, 250)]):
        self.punkts = punkts
    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self, ai_settings, screen):
        done = True
        font_menu = pygame.font.Font("fonts/10672.ttf", 50)
        punkt = 0
        while done:
            # Цвет основного экрана
            screen.fill(ai_settings.bg_color)
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
            screen.blit(screen, (0, 0))
            # Отображение последнего прорисованного экрана.
            pygame.display.flip()