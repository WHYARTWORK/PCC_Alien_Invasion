import pygame

def run_game():
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.Font(None, 30)
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode(
        (screen_width, screen_height))
    pygame.display.set_caption("Printing Game")
    bg_color = (0,0,0)
    Blue = (76,45,7)
    user_input = ''

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                user_input += str(event)
        screen.fill(bg_color)
        text = myfont.render(user_input, True, Blue)
        screen.blit(text,(20, 20))
        pygame.display.flip()

run_game()
