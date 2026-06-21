import pygame;

# Window Size
WIN_WIDTH = 576
WIN_HEIGHT = 324

# Pallet Colors
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

# Menu Options
MENU_OPTIONS = [
    "NEW GAME 1P",
    "NEW GAME 2P - COOPERATIVE",
    "NEW GAME 2P - COMPETITIVE",
    "SCORE",
    "EXIT"
]

# Player Options
PLAYER_SPEED = 2

PLAYER_KEY_UP = {"Player1": pygame.K_UP, "Player2": pygame.K_w}
PLAYER_KEY_DOWN = {"Player1": pygame.K_DOWN, "Player2": pygame.K_s}
PLAYER_KEY_LEFT = {"Player1": pygame.K_LEFT, "Player2": pygame.K_a}
PLAYER_KEY_RIGHT = {"Player1": pygame.K_RIGHT, "Player2": pygame.K_d}

# Enemy Options
ENEMY1_SPEED = 2
ENEMY2_SPEED = 1
ENEMY_EVENT = pygame.USEREVENT + 1