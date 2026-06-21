import pygame

from abc import ABC, abstractmethod

class Entity(ABC):

    def __init__(self, name: str, position: tuple, speed=0):
        self.name = name;
        self.position = position;
        self.surf = pygame.image.load(f"./assets/{self.name}.png").convert_alpha();
        self.rect = self.surf.get_rect(left=position[0], top=position[1]);
        self.speed = speed;

    @abstractmethod
    def move(self):
        pass;