import string
import pygame
import gettext
import ptext

from os import putenv

from src.tools import fill_gradient

gettext.install('translations', 'locale', codeset='UTF-8', names=['ngettext'])

# pl = gettext.translation('translations', localedir='locale', languages=['pl'])
# pl.install()

print(_('This message is in the script.'))

putenv("SDL_VIDEO_WINDOW_POS", "")
putenv("SDL_VIDEO_CENTERED", "1")

DEBUG = False

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Butterfly Mind - logic game')
clock = pygame.time.Clock()
FONT_PATH = 'fonts/KR Butterfly.ttf'
FONT_PATH2 = 'fonts/KR Butterflies.ttf'
FONT_SIZE_BIG = 140
FONT_SIZE_MEDIUM = 72
FONT_SIZE_SMALL = 48
purple = (255, 0, 255)
purple2 = (255, 0, 150)
darkolivegreen = (85, 107, 47)
deeppink = (255, 20, 147)
hotpink = (255, 105, 180)
darkviolet = (148, 0, 211)
pink = (255, 192, 203)


# all_fonts = pygame.font.get_fonts()
# font = pygame.font.SysFont("padauk", 72)
# font = pygame.font.Font(FONT_PATH, 92)

# text1 = font.render("Butterfly", True, purple2)
# text2 = font.render("Mind", True, purple)


def welcome():
    print(_('Starting WELCOME screen...'))

    butterflies = [
        # generate_random_str(),
        # generate_random_str(),
        # generate_random_str()
        "A B  C  F G  H",
        "I  J K  L   M ",
        "E    F  P ",
    ]

    tick = 0
    done = False
    start_game = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                done = True
                start_game = True

        # screen.fill((255, 255, 255))
        # screen.fill((0, 30, 60))
        # if tick > 10:
        # tick += 1
        # if tick > 50:
        #     screen_fill = purple
        #     tick = 0
        # else:
        #     screen_fill = purple2

        # screen_fill = darkolivegreen
        # screen.fill(screen_fill)
        fill_gradient(screen, darkviolet, purple)

        b_line = 50
        for butterflly in butterflies:
            ptext.draw(butterflly,
                       center=(screen.get_height() // 2 + 120, b_line), fontname=FONT_PATH2,
                       fontsize=FONT_SIZE_MEDIUM, shadow=(1, 1),
                       color="yellow", gcolor="hotpink", owidth=1.5, ocolor="black", alpha=0.3)
            b_line += 90

        ptext.draw(_("Butterfly\nMind"),
                   center=(screen.get_height() // 2 + 120, screen.get_width() // 2 - 100), fontname=FONT_PATH,
                   fontsize=FONT_SIZE_BIG,
                   color="black", gcolor="red", owidth=1.5, ocolor="hotpink", alpha=0.8)

        ptext.draw(_("Press ENTER to PLAY"),
                   center=(screen.get_height() // 2 + 120, screen.get_width() // 2 + 150), fontname=FONT_PATH,
                   fontsize=FONT_SIZE_SMALL, shadow=(2, 2),
                   color=(255, 255, 255), gcolor=pink, owidth=1.5, ocolor="black", alpha=0.8)

        if DEBUG:
            text = "\n".join([
                "F2: toggle DEBUG mode",
                "F10: toggle portrait mode",
                "F11: toggle fullscreen",
                "F12: screenshot",
                "%.1ffps" % clock.get_fps(),
            ])
            ptext.draw(text, bottomleft=(screen.get_height() - 50, 150), fontsize=32, color="white")
        pygame.display.flip()
        clock.tick(60)

    return start_game
