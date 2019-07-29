import pygame
from pygame.sprite import Sprite

class Passage(Sprite):
    def __init__(self, ai_settings, screen):
        """Инициализирует комнату и задает его начальную позицию."""
        super(Passage, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения Комнаты и получение прямоугольника.
        self.image = pygame.image.load('images/passage_1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждая новая комната появляется в центре.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        #self.rect.x = self.rect.width
        #self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Рисует комнату в текущей позиции."""
        self.screen.blit(self.image, self.rect)