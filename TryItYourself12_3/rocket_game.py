import pygame

from rocket_settings import Settings
from rocket_ship import Ship
import rocket_game_functions as gf

def run_game():
    #Initialize the modules
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Rocket Game")

    #Draw a ship.
    ship = Ship(ai_settings, screen)

    #Start the loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
