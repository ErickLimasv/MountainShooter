from packages.Entity import Entity

class Enemy(Entity):

    def __init__(self, name: str, position: tuple, speed):
        super().__init__(name, position, speed)

    def move(self):
        self.rect.centerx -= self.speed