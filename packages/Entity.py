import pygame

from abc import ABC, abstractmethod

class Entity(ABC):

    def __init__(self, surf: str, position: tuple):
        self.surf = surf;
        self.position = position;
        self.surf = pygame.image.load("./assets/" + self.surf);
        self.rect = self.surf.get_rect(left=position[0], top=position[1]);
        self.speed = 0;

    @abstractmethod
    def move(self):
        pass;