class Settings():
    """class save all setings for game AllienInvasion"""

    def __init__(self):
        """initial setiings game"""
        #screnn params
        self.screen_width = 700
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        #ship settings
        self.ship_speed = 1.5
        #bullet params
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_speed = 2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.ship_limit = 3
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """init settings turned in play game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.fleet_direction = 1
        self.alien_points = 1

    def increase_speed(self):
        """upper settings game speed"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)