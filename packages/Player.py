import pygame;

from packages.Const import WIN_WIDTH, WIN_HEIGHT, PLAYER_SPEED, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT
from packages.Entity import Entity

class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[PLAYER_KEY_UP[self.name]]:
            if self.rect.top > 0:
                self.rect.centery -= PLAYER_SPEED
        if pressed_key[PLAYER_KEY_DOWN[self.name]]:
            if self.rect.bottom < WIN_HEIGHT:
                self.rect.centery += PLAYER_SPEED  
        if pressed_key[PLAYER_KEY_LEFT[self.name]]:
            if self.rect.left > 0:
                self.rect.centerx -= PLAYER_SPEED
        if pressed_key[PLAYER_KEY_RIGHT[self.name]]:
            if self.rect.right < WIN_WIDTH:
                self.rect.centerx += PLAYER_SPEED