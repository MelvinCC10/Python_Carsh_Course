import sys
import pygame as pg

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

    # Start main loop of game.
    while True:
        gf.check_event(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)



run_game()
