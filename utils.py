import random
import pygame
from config import *

class Utils:
    
    @staticmethod
    def get_random_pos() -> pygame.Vector2:
        return pygame.Vector2(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
    
    @staticmethod
    def get_random_vel() -> pygame.Vector2:
        return pygame.Vector2(random.uniform(MIN_RANDOM_VEL, MAX_RANDOM_VEL), random.uniform(MIN_RANDOM_VEL, MAX_RANDOM_VEL))