import pygame as pg

class Ship():

    def __init__(self, screen):
        """ Initialize the ship ans sets its Start position."""
        self.screen = screen

        # Load the ship image and get set its rect.
        self.image = pg.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement Flag
        self.moving_right = False

    def update(self):
        """ Update the ships position based on the movement flag. """
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """ draw the ship at its current location """
        self.screen.blit(self.image, self.rect)
