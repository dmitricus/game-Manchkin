import sys
import pygame
from settings import Settings
from data.room import Room
from data.passage import Passage
from config import *
from die import Die



ai_settings = Settings()
count_room = 1
health = 5
number_of_moves = 1


def check_keydown_events(event, passage):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_RIGHT:
        passage.moving_right = True
    elif event.key == pygame.K_LEFT:
        passage.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, passage):
    """Реагирует на отпускание клавиш."""
    if event.key == pygame.K_RIGHT:passage.moving_right = False
    elif event.key == pygame.K_LEFT:passage.moving_left = False


def check_events(stats, WINDOW, SCREEN, play_button, exit_button):
    screen_rect = SCREEN.get_rect()
    centerx = screen_rect.centerx
    centery = screen_rect.centery

    play_button_width = exit_button.rect.width
    play_button_height = exit_button.rect.height

    exit_button_width = exit_button.rect.width
    exit_button_height = exit_button.rect.height

    # Ширина прохода
    passage_width = 84
    # Высота прохода
    passage_height = 110

    # Ширина комнаты
    room_width = 226
    # Высота комнаты
    room_height = 226

    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                stats.game_active = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print("X {} Y {}".format(mouse_x, mouse_y))


            if not stats.game_active:
                # Кнопка меню Старт
                if mouse_x >= (centerx - play_button_width/2) and mouse_y >= (centery - play_button_height/2):
                    if mouse_x <= (centerx + play_button_width/2) and mouse_y <= (centery + play_button_height/2):
                        stats.game_active = True
                        check_play_button(stats, play_button, mouse_x, mouse_y)
                # Кнопка меню Выход
                if mouse_x >= (centerx - play_button_width/2) and mouse_y >= (centery + play_button_height - exit_button_height/2 + 10):
                    if mouse_x <= (centerx + play_button_width/2) and mouse_y <= (centery + play_button_height + exit_button_height/2 + 10):
                        stats.game_active = False
                        check_exit_button(exit_button, mouse_x, mouse_y)

            elif stats.game_active:
                # Центральная комната
                if mouse_x >= (centerx - room_width/2) and mouse_y >= (centery - room_height/2):
                    if mouse_x <= (centerx + room_width/2) and mouse_y <= (centery + room_height/2):
                        print("Центральная комната!")
                        pos = pygame.mouse.get_pos()
                        # Бросок кубика
                        # Создание кубика D6.
                        die = Die()
                        number_of_moves = die.roll()
                        print("Бросок кубика D6 = " + str(number_of_moves))


                # Проход влево 1
                if mouse_x >= (centerx - passage_width - room_width/2) and mouse_y >= (centery - passage_height/2):
                    if mouse_x <= (centerx - room_width/2) and mouse_y <= (centery + passage_height/2):
                        print("Проход Влево 1")
                # Проход вправо 1
                if mouse_x >= (centerx + room_width/2) and mouse_y >= (centery - passage_height/2):
                    if mouse_x <= (centerx + passage_width + room_width/2) and mouse_y <= (centery + passage_height/2):
                        print("Проход Вправо 1")
                # Проход вверх 1
                if mouse_x >= (centerx - passage_height/2) and mouse_y >= (centery - passage_width - room_height/2):
                    if mouse_x <= (centerx + passage_height/2) and mouse_y <= (centery - room_height/2):
                        print("Проход Вверх 1")
                # Проход вниз 1
                if mouse_x >= (centerx - passage_height/2) and mouse_y >= (centery + room_height/2):
                    if mouse_x <= (centerx + passage_height/2) and mouse_y <= (centery + passage_width + room_height/2):
                        print("Проход Вниз 1")

                # Левая комната 1
                if mouse_x >= (centerx - passage_width - room_width - room_width/2) and mouse_y >= (centery - room_height/2):
                    if mouse_x <= (centerx - passage_width - room_width/2) and mouse_y <= (centery + room_height/2):
                        print("Левая комната 1")
                # Правая комната 1
                if mouse_x >= (centerx + passage_width + room_width/2) and mouse_y >= (centery - room_height/2):
                    if mouse_x <= (centerx + passage_width + room_width + room_width/2) and mouse_y <= (centery + room_height/2):
                        print("Правая комната 1")
                # Верхняя комната 1
                if mouse_x >= (centerx - room_width/2) and mouse_y >= (centery - passage_width - room_width - room_width/2):
                    if mouse_x <= (centerx + room_width/2) and mouse_y <= (centery - passage_width - room_width/2):
                        print("Верхняя комната 1")
                # Нижняя комната 1
                if mouse_x >= (centerx - room_width/2) and mouse_y >= (centery + passage_width + room_width/2):
                    if mouse_x <= (centerx + room_width/2) and mouse_y <= (centery + passage_width + room_width + room_width/2):
                        print("Нижняя комната 1")



def check_play_button(stats, play_button, mouse_x, mouse_y):
    """Запускает новую игру при нажатии кнопки Play."""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True

def check_exit_button(exit_button, mouse_x, mouse_y):
    """Завершает игру при нажатии кнопки Exit."""
    if exit_button.rect.collidepoint(mouse_x, mouse_y):
        pygame.quit()
        sys.exit()


def update_screen(ai_settings, SCREEN, rooms, passages, stats, play_button, exit_button):
    """Обновляет изображения на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран.
    SCREEN.fill(ai_settings.bg_color)
    # Кнопка Play отображается в том случае, если игра неактивна.
    if not stats.game_active:
        play_button.draw_button()
        exit_button.draw_button()
    #room.blitme()
    if stats.game_active:
        # Нарисовать на экране несколько черных линий от (0,10) до (100,110)
        # шириной в пять пикселей, используя цикл for
        #for x in range(30, ai_settings.screen_width, 25):
        #    pygame.draw.line(SCREEN, BLACK, [x, 30], [x, ai_settings.screen_width], 1)

        #for x in range(30, ai_settings.screen_width, 25):
        #    pygame.draw.line(SCREEN, BLACK, [30, x], [ai_settings.screen_width, x], 1)

        # Выбрать шрифт для использования.
        # Стандартный шрифт, размером в 25.
        font = pygame.font.Font(None, 25)

        # Воспроизвести текст. "True" значит,
        # что текст будет сглаженным (anti-aliased).
        # Чёрный - цвет. Переменную BLACK мы задали ранее,
        # списком [0,0,0]
        # Заметьте: эта строка создаёт картинку с буквами,
        # но пока не выводит её на экран.
        text = font.render("Health: " + str(health), True, BLACK)
        # Вывести сделанную картинку на экран в точке (250, 250)
        SCREEN.blit(text, [10, 10])

        message = font.render("Количество ходов: " + str(number_of_moves), True, BLACK)
        SCREEN.blit(message, [10, 30])

        rooms.draw(SCREEN)
        passages.draw(SCREEN)

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()

def create_room(ai_settings, screen, rooms):
    # Ширина прохода
    passage_width = 84
    # Высота прохода
    passage_height = 110
    screen_rect = screen.get_rect()
    centerx = screen_rect.centerx
    centery = screen_rect.centery
    """Создает комнату и размещает ее на поле по заданным координатам"""
    room = Room(ai_settings, screen)
    # Ширина комнаты
    room_width = room.rect.width
    # Высота комнаты
    room_height = room.rect.height
    #print("Ширина комнаты {} Высота комнаты {}".format(room_width, room_height))
    print("Ширина экрана {} Высота экрана {}".format(ai_settings.screen_width, ai_settings.screen_height))
    available_space_x = ai_settings.screen_width - 2 * room_width
    available_space_y = ai_settings.screen_height - 2 * room_height
    #print("Доступное пространство X {} Доступное пространство Y {}".format(available_space_x, available_space_y))
    #print(available_space_x / (2 * room_width))
    # number_rooms_x = int(available_space_x / (2 * room_width))
    number_rooms_x = 5
    # Создание первого прохода вокруг комнаты.
    for room_number in range(number_rooms_x):
        # Создание прохода и размещение ее вычисляемое положение вокруг комнаты.
        room = Room(ai_settings, screen)
        # Центральная комната
        if room_number == 0:
            pass
        # вычисление для первого прохода с права
        if room_number == 1:
            room.x = centerx + (room_width/2) + passage_width
            room.rect.x = room.x
        # вычисление для первой комнаты слева
        if room_number == 2:
            room.x = centerx - room_width - (room_width/2) - passage_width
            room.rect.x = room.x
        # вычисление для первой комнаты сверху
        if room_number == 3:
            room.y = centery - room_height - (room_height/2) - passage_width
            room.x = centerx - (room_width/2)
            room.rect.x = room.x
            room.rect.y = room.y
        # вычисление для первой комнаты снизу
        if room_number == 4:
            room.y = centery + (room_height/2) + passage_width
            room.x = centerx - (room_width / 2)
            room.rect.x = room.x
            room.rect.y = room.y
        rooms.add(room)

def create_passages(ai_settings, screen, passages):
    # Ширина комнаты
    room_width = 226
    # Высота комнаты
    room_height = 226
    # определим центр поля
    screen_rect = screen.get_rect()
    centerx = screen_rect.centerx
    centery = screen_rect.centery
    """Создает проходы."""
    # Создание проходов.
    passage = Passage(ai_settings, screen)
    # Ширина прохода
    passage_width = passage.rect.width
    # Высота прохода
    passage_height = passage.rect.height
    #print("Ширина прохода {} Высота прохода {}".format(passage_width, passage_height))
    available_space_x = ai_settings.screen_width - 2 * passage_width
    available_space_y = ai_settings.screen_height - 2 * passage_height
    #print("Доступное пространство X {} Доступное пространство Y {}".format(available_space_x, available_space_y))
    #number_passages_x = int(available_space_x / (2 * passage_width))
    number_passages_x = 4
    # Создание первого прохода вокруг комнаты.
    for passage_number in range(number_passages_x):
        # Создание прохода и размещение ее вычисляемое положение вокруг комнаты.
        passage = Passage(ai_settings, screen)
        # вычисление для первого прохода с права
        if passage_number == 0:
            passage.x = centerx + (room_width/2)
            passage.rect.x = passage.x
            #print("Смещение прохода: centerx({}) + passage_width({}) + 30 = {}".format(centerx, passage_width, passage.x))
        # вычисление для первого прохода слева
        if passage_number == 1:
            passage.x = centerx - (room_width/2) - passage_width
            passage.rect.x = passage.x
        # вычисление для первого прохода сверху
        if passage_number == 2:
            passage.image = pygame.transform.rotate(passage.image, 90)
            passage.y = centery - (room_height/2) - passage_width
            #print("Смещение прохода по Y: centerx({}) + passage_width({}) = {}".format(centerx, passage_width, passage.y))
            passage.x = centerx - (passage_height/2)
            #print("Смещение прохода по X: centerx({}) - passage_height({}/2) = {}".format(centerx, passage_height, passage.x))
            passage.rect.x = passage.x
            passage.rect.y = passage.y
        # вычисление для первого прохода снизу
        if passage_number == 3:
            passage.image = pygame.transform.rotate(passage.image, 90)
            passage.y = centery + (room_height / 2)
            #print("Смещение прохода по Y: centerx({}) + passage_width({}) = {}".format(centerx, passage_width, passage.y))
            passage.x = centerx - (passage_height/2)
            #print("Смещение прохода по X: centerx({}) - passage_height({}/2) = {}".format(centerx, passage_height, passage.x))
            passage.rect.x = passage.x
            passage.rect.y = passage.y

        passages.add(passage)