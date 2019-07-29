#-------------------------------------------------------------------------------
# Imports & Inits
import pygame
from settings import Settings
import game_functions as gf
from game_stats import GameStats
from button import Button

from pygame.sprite import Group
#-------------------------------------------------------------------------------
# Settings
ai_settings = Settings()
WIDTH = ai_settings.screen_width
HEIGHT = ai_settings.screen_height
FPS = 60
#-------------------------------------------------------------------------------
# Screen Setup
WINDOW = pygame.display.set_mode([WIDTH, HEIGHT])
CAPTION = pygame.display.set_caption("Манчкин Квест")
SCREEN = pygame.display.get_surface()
#-------------------------------------------------------------------------------
# Refresh Display
pygame.display.flip()
#-------------------------------------------------------------------------------
# Main Loop
def run_game():
    # Инициализирует pygame, settings и объект экрана.
    pygame.init()

    # Создание экземпляра для хранения игровой статистики.
    stats = GameStats(ai_settings)

    # Создание кнопки Play.
    play_button = Button(ai_settings, SCREEN, "Старт", 50, 0)
    # Создание кнопки Exit.
    exit_button = Button(ai_settings, SCREEN, "Выход", 50, 60)


    # Создание комнаты.
    #room = Room(ai_settings, SCREEN)

    # Создание прохода.
    #passage = Passage(ai_settings, SCREEN)

    # Создание группы для хранения комнат.
    rooms = Group()
    passages = Group()

    # Создание группы комнат.
    gf.create_room(ai_settings, SCREEN, rooms)
    # Создание группы проходов.
    gf.create_passages(ai_settings, SCREEN, passages)

    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(stats, WINDOW, SCREEN, play_button, exit_button)
        gf.update_screen(ai_settings, SCREEN, rooms, passages, stats, play_button, exit_button)



run_game()