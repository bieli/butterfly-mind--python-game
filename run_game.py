import sys

import pygame

from src.resources import Resources
from src.game import start
from src.welcome import welcome
from src.score import score
from os import putenv


SCREEN_X, SCREEN_Y = 1024, 768
GAME_CAPTION = 'Butterfly Mind - logic game for girls & geeks :-)'

if __name__ == '__main__':
    putenv("SDL_VIDEO_CENTERED", "1")
    putenv("SDL_VIDEO_WINDOW_POS", "")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
    pygame.display.set_caption(GAME_CAPTION)

    resources = Resources(pygame, screen)

    try:
        while True:
            start_game, mode = welcome(resources)
            if start_game:
                points = start(resources, mode)
                if points:
                    points = score(points)
    except SystemExit:
        sys.exit(0)
