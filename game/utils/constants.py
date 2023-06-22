import pygame
import os
pygame.mixer.init()
# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/Batery.png'))

START_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/start_sound.wav"))

GAME_OVER_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/game_over_sound.wav"))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/laser.wav"))
SPACESHIP_EXPLOSION = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/player_explosion.wav"))
MEGA_LASER = pygame.image.load(os.path.join(IMG_DIR, 'Other/laser_power_up.png'))
LASER_POWER_UP = pygame.image.load(os.path.join(IMG_DIR, 'Other/Power_up_laser.png'))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/explosion.wav"))
ENEMY_SHOOT_SOUND = pygame.mixer.Sound(os.path.join(IMG_DIR, "Sounds/enemy_laser.wav"))

FONT_STYLE = 'freesansbold.ttf'
