import random

from packages.Const import WIN_WIDTH, WIN_HEIGHT, ENEMY1_SPEED, ENEMY2_SPEED;
from packages.Background import Background;
from packages.Player import Player;
from packages.Enemy import Enemy;

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case "Level1":
                list_background = [];
                for i in range(7):
                    list_background.append(Background(f"Level1Bg{i}", i))
                    list_background.append(Background(f"Level1Bg{i}", i, position=(WIN_WIDTH, 0)))
                return list_background
            case "Player1":
                return Player("Player1", (20, WIN_HEIGHT/2))
            case "Player2":
                return Player("Player2", (20, WIN_HEIGHT/2 - 40))
            case "Enemy1":
                return Enemy("Enemy1", (WIN_WIDTH, random.randint(40, WIN_HEIGHT-40)), ENEMY1_SPEED)
            case "Enemy2":
                return Enemy("Enemy2", (WIN_WIDTH, random.randint(40, WIN_HEIGHT-40)), ENEMY2_SPEED)