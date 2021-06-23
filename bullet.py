import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for manage bullet from ships"""
    def __init__(self, ai_game):
        """create new object bullet in this positions"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #create bullet in pos (0,0) and take new pos
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        #pos bullet save in float form
        self.y = float(self.rect.y)

    def update(self):
        """moving bullet upscreen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet in screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)