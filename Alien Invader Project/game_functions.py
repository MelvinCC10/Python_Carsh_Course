import sys

import pygame as pg

def check_event(ship):
    """ Respond to keypresses and mouse events. """
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                ship.moving_right = True
            elif event.key == pg.K_LEFT:
                ship.moving_left = True

        elif event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                ship.moving_right = False
            elif event.key == pg.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings,screen, ship):
    """ Update images on the screen and flip to the new screen """
    # Redraw the screen dring each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pg.display.flip()
