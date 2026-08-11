import pygame
from config import *
from utils import Utils
from swarm_behaviour import SwarmBehaviour

class Agent(SwarmBehaviour):
    def __init__(self) -> None:
        super().__init__()
        
        self.game_width = SCREEN_WIDTH
        self.game_height = SCREEN_HEIGHT
        self.pos = pygame.Vector2(Utils.get_random_pos())
        self.vel =  pygame.Vector2(Utils.get_random_vel())
        self.color = AGENT_COLOR