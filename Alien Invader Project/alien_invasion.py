import sys

import pygame as pg

def run_game():
    #Initialize game and create a screen object
    pg.init()
    screen = pg.display.set_mode((1200, 800))
    pg.display.set_caption("Alien Invasion")

    # set the background color
    bg_color = (230, 230, 230)

    # Start main loop of game.
    while True:

        #Watch for keyboard and mouse events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        # Redraw the screen dring each pass through the loop
        screen.fill(bg_color)

        # Make the most recently drawn screen visible
        pg.display.flip()

run_game()
