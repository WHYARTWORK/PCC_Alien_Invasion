class Settings():
    """Stores settings for rocket game"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0,0,0)

        # Ship settings
        self.ship_speed_mult = 2
