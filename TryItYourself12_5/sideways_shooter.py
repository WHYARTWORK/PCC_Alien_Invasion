import pygame

from sideways_settings import Settings
from sideways_ship import Ship
import sideways_game_function as gf
from pygame.sprite import Group

def run_game():
    #Initialize the modules
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Rocket Game")

    #Draw a ship.
    ship = Ship(ai_settings, screen)

    #Make a group to store bullets in.
    bullets = Group()

    #Start the loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
