import pygame;

from packages.Const import *;

class Menu:

    def __init__(self, window):
        self.window = window;
        self.surf = pygame.image.load('./assets/MenuBg.png').convert_alpha();
        self.rect = self.surf.get_rect(left=0, top=0);

    def run(self):
        pygame.mixer_music.load("./assets/Menu.mp3");
        pygame.mixer_music.play(-1);

        while True:
            self.window.blit(source=self.surf, dest=self.rect);

            self.menu_text(60, "Mountain", COLOR_ORANGE, (WIN_WIDTH/2, 50));
            self.menu_text(60, "Shooter", COLOR_ORANGE, (WIN_WIDTH/2, 90));

            for i in range(len(MENU_OPTIONS)):
                self.menu_text(30, MENU_OPTIONS[i], COLOR_WHITE, (WIN_WIDTH/2, 180 + 30 * i));

            pygame.display.flip();

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit();
                    print("Game Closed")
                    quit();

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font = pygame.font.SysFont("Lucida Sans Typewriter", text_size);
        text_surf = font.render(text, True, text_color);
        text_rect = text_surf.get_rect(center=text_center_pos);
        self.window.blit(source=text_surf, dest=text_rect);