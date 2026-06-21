import pygame;

from packages.Entity import Entity
from packages.Menu import Menu
from packages.EntityFactory import EntityFactory;

class Level:

    def __init__(self, window, name: str, game_mode: int):
        self.window = window;
        self.name = name;
        self.game_mode = game_mode;
        self.entity_list: list[Entity] = [];
        self.entity_list.extend(EntityFactory.get_entity(self.name));

    def run(self):

        while True:
            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect);
                entity.move();
            pygame.display.flip();

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Menu.game_exit(self.window);