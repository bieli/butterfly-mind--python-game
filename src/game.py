import random
from random import randint

import pygame
import ptext
from src.tools import generate_random_str, make_new_game_obj

pygame.init()
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
elasped_seconds = 120
FONT_PATH = 'fonts/KR Butterfly.ttf'
FONT_PATH2 = 'fonts/KR Butterflies.ttf'
FONT_PATH_KEYS = 'fonts/KeyCapsFLF.ttf'
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
springgreen = (0, 255, 127)
limegreen = (50, 205, 50)
darkgreen = (0, 100, 0)
last_str = ''


def new_positions(pattern='ABCDEFGHIJLMNOP', max=3):
    global last_str
    positions = []
    step = 300
    for pos in range(max):
        rx = step - 200
        ry = step + 50
        xy = randint(rx, ry)
        # print("\n-----\n", rx, ry, xy)
        positions.append(xy)
        step += 150
    # return [randint(100, 300), randint(350, 500), randint(550, 700)], generate_random_str(pattern, max=max)
    str = generate_random_str(allchar=pattern, max=max)
    if len(last_str):
        str = last_str
    rnd_choice = random.choice([ch for ch in str])
    new_str = make_new_game_obj(str, rnd_choice, allchars=pattern)
    print(str, new_str, rnd_choice)
    last_str = new_str
    return positions, new_str, rnd_choice


def show(resources, pos, alpha_value, generated_objects, mode):
    b_line = 250
    pos_no = 0

    for butterflly in generated_objects:
        shadow = (0, 0)
        if mode == 1:
            fontname = resources.FONT_PATH
        elif mode == 2:
            fontname = resources.FONT_PATH2
        elif mode == 3:
            shadow = (1, 1)
            fontname = resources.FONT_PATH2

        ptext.draw(butterflly,
                   center=(resources.get_screen().get_height() // 2 - 150 + pos[pos_no], b_line), fontname=fontname,
                   fontsize=resources.FONT_SIZE_BIG, shadow=shadow,
                   color="pink", owidth=0.4, ocolor="red", alpha=alpha_value)

        ptext.draw("{}".format(pos_no + 1),
                   center=(resources.get_screen().get_height() // 2 - 300, b_line + 20),
                   fontname=resources.FONT_PATH_KEYS,
                   fontsize=resources.FONT_SIZE_BIG, shadow=(0, 0),
                   color="gray", owidth=0.2, ocolor="black", alpha=0.5)
        b_line += 150
        pos_no += 1


def start(resources, mode):
    global elasped_seconds
    print('Starting GAME screen...')

    points = -1
    clicks = 0
    done = False
    pygame.display.update()

    pos, gen, rnd_choice = new_positions()

    bg = pygame.image.load("resources/img/bg1.jpg")

    alpha_value = 1.0
    while not done:
        if elasped_seconds <= 0:
            print("Points: {}".format(points))
            print("Clicks: {}".format(clicks))
            done = True
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                elasped_seconds -= 1
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                raise SystemExit(points)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # alpha_value = 0.0
                pos, gen, rnd_choice = new_positions()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                pressed_key = 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                pressed_key = 2
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                pressed_key = 3
            else:
                pressed_key = 0

            if pressed_key:
                if points < 0:
                    points = 0
                else:
                    print(" pressed_key: {}".format(pressed_key))
                    clicks += 1
                    selected = gen[pressed_key - 1]
                    choice = 'BAD'
                    if rnd_choice == selected:
                        choice = 'GOOD'
                        points += 10
                    print(" - {} choice: {}".format(choice, selected))
                pos, gen, rnd_choice = new_positions()

        resources.get_screen().blit(bg, (0, 100))

        show(resources, pos, alpha_value, gen, mode)

        ptext.draw("Butterfly Mind",
                   center=(resources.get_screen().get_height() // 2 + 120,
                           resources.get_screen().get_width() // 2 - 470),
                   fontname=resources.FONT_PATH,
                   fontsize=resources.FONT_SIZE_MEDIUM,
                   color="purple", gcolor="red", owidth=1.5, ocolor="hotpink", alpha=1.0)

        ptext.draw("Credits: {}".format(points), bottomleft=(resources.get_screen().get_height() // 2 + 220,
                                                             resources.get_screen().get_width() // 2 - 330),
                   fontsize=64,
                   color="purple", gcolor="purple2", owidth=0.8, ocolor="hotpink", alpha=1.0)

        ptext.draw("Seconds: {}".format(elasped_seconds), bottomleft=(resources.get_screen().get_height() // 2 - 220,
                                                                      resources.get_screen().get_width() // 2 - 330),
                   fontsize=64,
                   color="purple", gcolor="purple2", owidth=0.8, ocolor="hotpink", alpha=1.0)

        pygame.display.flip()
        clock.tick(60)

    return points
