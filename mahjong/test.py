import sys
import pygame as pg
from mahjong import mahjong


def func(card):
    pg.init()

    screen = pg.display.set_mode((1600, 900))

    screen.fill((0, 100, 0))

    pg.display.set_caption('MahJong')

    cardImage = pg.image.load(f'image/128/fulltiles/{card}.png').convert_alpha()
    # card = pg.image.load(f'image/128/fulltiles/white.png').convert()
    # cimage.fill((0, 0, 255), special_flags=0)
    # cimage.scroll(100, 50)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        # pg.display.flip()
        screen.blit(cardImage, (0, 600))
        pg.display.update()
