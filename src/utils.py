import random
import pygame
from config import *


class Utils:
    """
    Provides helper methods used when creating agents.
    """

    @staticmethod
    def get_random_pos() -> pygame.Vector2:
        """Return a random position inside the simulation window."""
        return pygame.Vector2(
            random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
        )

    @staticmethod
    def get_random_vel() -> pygame.Vector2:
        """
        Return a random initial velocity.
        """

        return pygame.Vector2(
            random.uniform(MIN_RANDOM_VEL, MAX_RANDOM_VEL),
            random.uniform(MIN_RANDOM_VEL, MAX_RANDOM_VEL),
        )
