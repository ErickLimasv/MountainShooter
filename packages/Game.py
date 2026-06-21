import pygame;
from packages.Menu import Menu;
from packages.Level import Level;
from packages.Entity import Entity;
from packages.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS;

class Game:
    def __init__(self):
        pygame.init();
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT));
        print("Game Opened")

    def run(self):
        while True:
            menu = Menu(self.window);
            menu_option = menu.run();

            if menu_option in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]:
                level = Level(self.window, "Level1", menu_option);
                level.run();
            elif menu_option == MENU_OPTIONS[-1]:
                menu.game_exit();
