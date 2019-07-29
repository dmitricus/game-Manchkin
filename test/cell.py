# -*-coding: utf8-*-
import pygame
import sys

SCALE = 10
screen = None


def set_mode(size, bcolor=[200, 200, 200], scale=100):
    """
    Создает окно заданного размера
    :param size: размеры окна в клетках
    :param bcolor: цвет границ
    :param scale: размер клеток (10 пикс. по дефолту)
    :return: "холст" окна
    """
    global SCALE, screen
    SCALE = scale
    screen = pygame.display.set_mode([size[0] * SCALE, size[1] * SCALE])
    for i in range(0, size[0]):
        pygame.draw.line(screen, bcolor, [i * SCALE, 0], [i * SCALE, size[1] * SCALE])
    for i in range(0, size[1]):
        pygame.draw.line(screen, bcolor, [0, i * SCALE], [size[0] * SCALE, i * SCALE])
    return screen


def fill(screen_color, bcolor=[200, 200, 200]):
    """
    Заливает окно цветом
    :param screen_color: цвет окна
    :param bcolor: цвет границ
    """
    global screen
    surface = screen
    surface.fill(screen_color)
    w, h = surface.get_size()
    for i in range(0, w):
        pygame.draw.line(surface, bcolor, [i * SCALE, 0], [i * SCALE, h * SCALE])
    for i in range(0, h):
        pygame.draw.line(surface, bcolor, [0, i * SCALE], [w * SCALE, i * SCALE])


def draw_point(surface, color, pos):
    """
    Закрашивает клеточку
    :param surface: поверхность (окно, например)
    :param color: цвет
    :param pos: координаты клетки
    """
    return pygame.draw.rect(surface, color, [pos[0] * SCALE, pos[1] * SCALE,  SCALE, SCALE])

while True:
    set_mode((10, 10))
    fill((50, 50, 50))
    draw_point(screen, (200, 200, 200), (5, 5))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()