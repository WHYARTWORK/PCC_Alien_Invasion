class Settings():
    """Stores settings for rocket game"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (250, 250, 250)

        # Ship settings
        self.ship_speed_mult = 2

        #Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 15
