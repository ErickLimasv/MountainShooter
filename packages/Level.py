import pygame;
import random;

from packages.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTIONS, ENEMY_EVENT
from packages.Entity import Entity
from packages.Menu import Menu
from packages.EntityFactory import EntityFactory

class Level:

    def __init__(self, window, name: str, game_mode: int):
        self.window = window;
        self.name = name;
        self.game_mode = game_mode;
        self.entity_list: list[Entity] = [];
        self.entity_list.extend(EntityFactory.get_entity("Level1"));
        self.entity_list.append(EntityFactory.get_entity("Player1"));
        self.timeout = 120000
         
        if game_mode in [MENU_OPTIONS[1], MENU_OPTIONS[2]]:
            self.entity_list.append(EntityFactory.get_entity("Player2"));
    
        pygame.time.set_timer(ENEMY_EVENT, 2000)
            

    def run(self):
        pygame.mixer_music.load(f"./assets/{self.name}.mp3");
        pygame.mixer_music.play(-1);

        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            for entity in self.entity_list:
                self.window.blit(source=entity.surf, dest=entity.rect);
                entity.move();
            
            self.level_text(14, f"FPS: {clock.get_fps() :.0f}", COLOR_WHITE, (30, WIN_HEIGHT-20))
            self.level_text(18, f"Time: {self.timeout/1000 :.0f}s", COLOR_WHITE, (40, 20))
            pygame.display.flip();

            for event in pygame.event.get():
                if event.type == ENEMY_EVENT:
                    choice = random.choice(("Enemy1", "Enemy2"))
                    self.entity_list.append(EntityFactory.get_entity(choice));
                if event.type == pygame.QUIT:
                    Menu.game_exit(self.window);

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font = pygame.font.SysFont("Lucida Sans Typewriter", text_size);
        text_surf = font.render(text, True, text_color);
        text_rect = text_surf.get_rect(center=text_center_pos);
        self.window.blit(source=text_surf, dest=text_rect);