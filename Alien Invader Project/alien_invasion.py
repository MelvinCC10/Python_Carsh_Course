import sys
import pygame as pg
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize game and create a screen object
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pg.display.set_caption("Alien Invasion")

    #make Ship
    ship = Ship(ai_settings,screen)
    #Make a group to store bullets in.
    bullets = Group()

    # Start main loop of game.
    while True:
        gf.check_event(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)



run_game()
