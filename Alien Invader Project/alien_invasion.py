import sys
import pygame as pg

from settings import Settings

def run_game():
    #Initialize game and create a screen object
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pg.display.set_caption("Alien Invasion")

    # Start main loop of game.
    while True:

        #Watch for keyboard and mouse events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        # Redraw the screen dring each pass through the loop
        screen.fill(ai_settings.bg_color)

        # Make the most recently drawn screen visible
        pg.display.flip()

run_game()
