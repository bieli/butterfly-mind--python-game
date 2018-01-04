import string

import pygame

from random import sample, randint


def remove_matches(text, to_remove):
    new = ""
    for ch in text:
        if ch not in to_remove:
            new = new + ch
    return new


def uniquify(text, maximum):
    output = []
    seen = set()
    for word in text:
        if maximum <= 0:
            break
        if word not in seen:
            output.append(word)
            seen.add(word)
            maximum -= 1
    return ''.join(output)


def uniques(your_string):
    words = your_string

    seen = set()
    seen_add = seen.add

    def add(x):
        seen_add(x)
        return x

    return ''.join(add(i) for i in words if i not in seen)


def generate_random_str(allchar="AB C D E  F G  H I ", max=None, exclude=None, unique=True):
    if max is None:
        max = len(allchar)
    else:
        randint(0, max)
    if exclude is not None:
        for char in exclude:
            allchar = allchar.replace(char, '')
    s = uniques(sample(allchar, max))
    # TODO: check faster method
    # s = "".join(choice(allchar) for _ in range(max))
    # s = "".join(sample(allchar, max))
    # s = uniquify(allchar, max)[:max]
    # s = uniquify(sample(allchar, max), max)
    # s = "".join(sample(sorted(set(allchar), key=allchar.index), max))
    # if len(exclude):
    #     excluded_char = False
    #     for n in range(max):
    #         if s.find(exclude[n]):
    #             s.replace(exclude[n], "")
    #             excluded_char = True
    #     if excluded_char:
    #         return generate_random_str(allchar=allchar, max=max, exclude=exclude)
    # else:

    if unique:
        unique_set = set([ch for ch in s])
        s = ''.join(unique_set)
        while len(s) != max:
            s = generate_random_str(allchar=allchar, max=max, exclude=exclude, unique=unique)
    return s


def make_new_game_obj(last_game_objects, last_selected_obj, allchars=string.ascii_uppercase):
    input_data = remove_matches(allchars, last_game_objects) + last_game_objects[:-1]
    new_rand = generate_random_str(allchar=input_data, max=3, exclude=last_game_objects[:-1])
    new_pair = new_rand[:-1]
    output = new_pair + last_selected_obj
    data = [[ch] for ch in output]
    # out = shuffle(data)
    return ''.join([ch[0] for ch in data])


def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
    """fill a surface with a gradient pattern
    Parameters:
    color -> starting color
    gradient -> final color
    rect -> area to fill; default is surface's rect
    vertical -> True=vertical; False=horizontal
    forward -> True=forward; False=reverse

    Pygame recipe: http://www.pygame.org/wiki/GradientCode
    """
    if rect is None:
        rect = surface.get_rect()
    x1, x2 = rect.left, rect.right
    y1, y2 = rect.top, rect.bottom
    if vertical:
        h = y2 - y1
    else:
        h = x2 - x1
    if forward:
        a, b = color, gradient
    else:
        b, a = color, gradient
    rate = (
        float(b[0] - a[0]) / h,
        float(b[1] - a[1]) / h,
        float(b[2] - a[2]) / h
    )
    fn_line = pygame.draw.line
    if vertical:
        for line in range(y1, y2):
            color = (
                min(max(a[0] + (rate[0] * (line - y1)), 0), 255),
                min(max(a[1] + (rate[1] * (line - y1)), 0), 255),
                min(max(a[2] + (rate[2] * (line - y1)), 0), 255)
            )
            fn_line(surface, color, (x1, line), (x2, line))
    else:
        for col in range(x1, x2):
            color = (
                min(max(a[0] + (rate[0] * (col - x1)), 0), 255),
                min(max(a[1] + (rate[1] * (col - x1)), 0), 255),
                min(max(a[2] + (rate[2] * (col - x1)), 0), 255)
            )
            fn_line(surface, color, (col, y1), (col, y2))
