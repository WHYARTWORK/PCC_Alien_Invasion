import pygame
class ShipTwo():

    def __init__(self, screen):
        """Initialize the ship and set its tarting position."""
        self.screen = screen

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
