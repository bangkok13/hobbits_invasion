import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """class for driving ships"""
    def __init__(self, ai_game):
        """init ship and sets the starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # load img ship adn create rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # all new ship appers near bottom screen
        self.rect.midbottom = self.screen_rect.midbottom
        #save x coordinate ship
        self.x = float(self.rect.x)
        #mooving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update position ship whith flag"""
        #update atrib x not rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """draw ship in position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
