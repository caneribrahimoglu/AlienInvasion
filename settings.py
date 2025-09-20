class Settings:
    """Uzayli istilasi icin butun ayarlari saklayan bir sinif"""
    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 1
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #filo yonu; 1 sagi -1 solu temsil etmektedir
        self.fleet_direction = 1


