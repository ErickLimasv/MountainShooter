from packages.Const import WIN_WIDTH
from packages.Entity import Entity;

class Background(Entity):

    def __init__(self, name: str, speed: int, position=(0,0)):
        super().__init__(name, position)
        self.speed = speed

    def move(self):
        self.rect.centerx -= self.speed;
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH;