import pygame
from config import *
from utils import Utils
from swarm_behaviour import SwarmBehaviour


class Agent(SwarmBehaviour):
    """
    Represents one individual agent in the swarm.

    Each agent has:
    - A position
    - A velocity
    - A color
    - Swarm behavior inherited from SwarmBehaviour.
    """

    def __init__(self) -> None:
        # Initialize the separation, alignment and cohesion behavior.
        super().__init__()

        # Generate a random starting position.
        self.pos = pygame.Vector2(Utils.get_random_pos())

        # Generate a random starting velocity.
        self.vel = pygame.Vector2(Utils.get_random_vel())

        # Set the agent's display color.
        self.color = AGENT_COLOR
