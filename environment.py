import pygame
from config import *

class Environment:
    
    def __init__(self, swarm: list) -> None:
        self.screen_width: int = SCREEN_WIDTH
        self.screen_height: int = SCREEN_HEIGHT
        self.swarm: list = swarm
        self.obstacle_positions = [pygame.Vector2(200, 200), 
                        pygame.Vector2(500, 300),
                        pygame.Vector2(800, 600),]
        self.wind_vec = pygame.Vector2(1, 0) 
        self.wind_strength = WIND_FORCE_STRENGTH
    
    def handle_boundaries(self) -> None:
        margin = 100 
        turn_stregth = 1.5
        max_correction = 3.0
        
        for agent in self.swarm:
            steer = pygame.Vector2(0, 0)
        
            if agent.pos.x < margin:
                strength = (1 - agent.pos.x / margin) * turn_stregth
                steer.x += min(strength, max_correction)
            elif agent.pos.x > self.screen_width - margin:
                strength = (1 - (self.screen_width - agent.pos.x) / margin) * turn_stregth
                steer.x -= min(strength, max_correction)
            
            if agent.pos.y < margin:
                strength = (1 - agent.pos.y / margin) * turn_stregth
                steer.y += min(strength, max_correction)
            elif agent.pos.y > self.screen_height - margin:
                strength = (1 - (self.screen_height - agent.pos.y) / margin) * turn_stregth
                steer.y -= min(strength, max_correction)
            
            agent.vel += steer
            
            agent.pos.x = max(0, min(self.screen_width, agent.pos.x))
            agent.pos.y = max(0, min(self.screen_height, agent.pos.y))
    
    def apply_obstacle_force(self) -> None:
        for agent in self.swarm:
            for obstacle_pos in self.obstacle_positions:
                dir_vec = agent.pos - obstacle_pos
                distance = dir_vec.length()
                
                interaction_radius = CIRCLE_OBSTACLE_RADIUS + 100
                
                if 0 < distance < interaction_radius:
                    dir_vec = dir_vec.normalize()
                
                    strength = REPULSION_STRENGTH * (1 - distance / interaction_radius)
                    force_vec = dir_vec * strength
                    agent.vel += force_vec * DT
    
    def apply_wind_force(self) -> None:
        for agent in self.swarm:
            agent.vel += self.wind_vec * self.wind_strength * DT