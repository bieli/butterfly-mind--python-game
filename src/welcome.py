import pygame
import ptext

from src.tools import fill_gradient


def welcome(resources, debug=False):
    print('Starting WELCOME screen...')

    butterflies = [
        "A B  C  F G  H",
        "I  J K  L   M ",
        "E    F  P ",
    ]

    done = False
    start_game = False
    mode = 1

    print("Selected MODE - default: EASY")

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                raise SystemExit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                done = True
                start_game = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                mode = 1
                print("Selected MODE - EASY")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                mode = 2
                print("Selected MODE - MEDIUM")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                mode = 3
                print("Selected MODE - HARD")

        fill_gradient(resources.get_screen(), resources.darkviolet, resources.purple)

        b_line = 50
        for butterflly in butterflies:
            ptext.draw(butterflly,
                       center=(resources.get_screen().get_height() // 2 + 120, b_line),
                       fontname=resources.FONT_PATH2,
                       fontsize=resources.FONT_SIZE_MEDIUM, shadow=(1, 1),
                       color="yellow", gcolor="hotpink", owidth=1.5, ocolor="black", alpha=0.3)
            b_line += 90

        ptext.draw("Butterfly\nMind",
                   center=(resources.get_screen().get_height() // 2 + 120,
                           resources.get_screen().get_width() // 2 - 300),
                   fontname=resources.FONT_PATH,
                   fontsize=resources.FONT_SIZE_BIG,
                   color="black", gcolor="red", owidth=1.5, ocolor="hotpink", alpha=0.8)

        i = 1
        for txt, pos in {'EASY': (100, 430), 'MEDIUM': (400, 430), 'HARD': (750, 430)}.items():
            x, y = pos
            ptext.draw("{}".format(i),
                       center=(x, y), fontname=resources.FONT_PATH_KEYS,
                       fontsize=resources.FONT_SIZE_SMALL, shadow=(0, 0),
                       color="gray", owidth=0.2, ocolor="black", alpha=0.5)
            ptext.draw("{}".format(txt),
                       midleft=(x + 40, y),
                       # fontname=resources.FONT_PATH2,
                       fontsize=resources.FONT_SIZE_SMALL, shadow=(2, 2),
                       color=(120, i * 60, i * 60), gcolor=resources.pink, owidth=1.5, ocolor="black", alpha=0.8)
            if i == 3:
                ptext.draw("BC",
                           center=(x + 80, y + 120),
                           fontname=resources.FONT_PATH2,
                           fontsize=resources.FONT_SIZE_BIG, shadow=(1, 1),
                           color="yellow", gcolor="hotpink", owidth=1.5, ocolor="black", alpha=0.6)
            elif i == 2:
                ptext.draw("BC",
                           center=(x + 80, y + 120),
                           fontname=resources.FONT_PATH2,
                           fontsize=resources.FONT_SIZE_BIG, shadow=(0, 0),
                           color="black", gcolor="black", owidth=0.5, ocolor="black", alpha=0.8)
            elif i == 1:
                ptext.draw("ABC",
                           center=(x + 80, y + 120),
                           fontname=resources.FONT_PATH,
                           fontsize=resources.FONT_SIZE_BIG, shadow=(0, 0),
                           color="pink", owidth=0.4, ocolor="hotpink", alpha=0.8)
            i += 1

        ptext.draw("Press ENTER to PLAY",
                   center=(resources.get_screen().get_height() // 2 + 120,
                           resources.get_screen().get_width() // 2 + 200),
                   fontname=resources.FONT_PATH,
                   fontsize=resources.FONT_SIZE_SMALL, shadow=(2, 2),
                   color=(255, 255, 255), gcolor=resources.pink, owidth=1.5, ocolor="black", alpha=0.8)

        if debug:
            text = "\n".join([
                "F2: toggle DEBUG mode",
                "F10: toggle portrait mode",
                "F11: toggle fullscreen",
                "F12: screenshot",
                "%.1ffps" % resources.get_clock().get_fps(),
            ])
            ptext.draw(text, bottomleft=(resources.get_screen().get_height() - 50, 150), fontsize=32, color="white")
        pygame.display.flip()
        resources.get_clock().tick(60)

    return start_game, mode
