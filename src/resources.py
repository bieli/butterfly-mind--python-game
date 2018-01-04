import pygame

FONTS_DIR = 'fonts'
IMAGES_DIR = 'imgs'


class Resources:
    _path_fonts = ()
    _images = ()
    _sprite_images = {}

    FONT_PATH = 'resources/fonts/KR Butterfly.ttf'
    FONT_PATH2 = 'resources/fonts/KR Butterflies.ttf'
    FONT_PATH_KEYS = 'resources/fonts/KeyCapsFLF.ttf'

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

    def __init__(self, pygame, screen, current_path=''):
        self.current_path = current_path
        self.screen = screen
        self.pygame = pygame
        self._load_fonts()
        self._load_images()

    def _load_fonts(self, sub_dir=FONTS_DIR):
        self._path_fonts, _ = self._discover_resources(sub_dir, 'ttf,oft')

    def _load_images(self, sub_dir=IMAGES_DIR):
        self._images, self._sprite_images = self._discover_resources(sub_dir, 'jpg,jpeg,png', with_subdir=True)
        for image_path in self._images:
            self._images[self._get_file_name(image_path)] = self.pygame.image.load(image_path)
        for sprite_name, image_sprite_path in self._sprite_images:
            self._images[(sprite_name, image_sprite_path)] = self.pygame.image.load(image_sprite_path)

    @staticmethod
    def _discover_resources(path, extensions, with_subdir=False):
        return (), ()

    @staticmethod
    def _get_file_name(image_path):
        return ''

    def get_font_path(self, name):
        return ''

    def get_image(self, name):
        return ()

    def get_sprite_image(self, sprite_name, image_name):
        return ()

    def get_clock(self):
        return pygame.time.Clock()

    def get_screen(self):
        return self.screen
