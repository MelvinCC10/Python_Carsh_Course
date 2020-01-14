import sys

import pygame as pg
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """ Respond to keypresses """
    if event.key == pg.K_RIGHT:
        ship.moving_right = True
    elif event.key == pg.K_LEFT:
        ship.moving_left = True
    elif event.key == pg.K_SPACE:
        #Create a new bullet and add it to the bullets Group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event,ship):
    """ Respond to keypresses """
    if event.key == pg.K_RIGHT:
        ship.moving_right = False
    elif event.key == pg.K_LEFT:
        ship.moving_left = False

def check_event(ai_settings, screen, ship, bullets):
    """Respoq to keypresses and mouse events """
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings,screen, ship, bullets):
    """ Update images on the screen and flip to the new screen """
    # Redraw the screen dring each pass through the loop
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # Make the most recently drawn screen visible
    pg.display.flip()
