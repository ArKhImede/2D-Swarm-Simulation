import pygame
from environment import Environment
from config import *
import math

class Visualization:
    
    def __init__(self, environment: Environment) -> None:
        self.screen_width: int = SCREEN_WIDTH
        self.screen_height: int = SCREEN_HEIGHT
        self.environment = environment
    
    def draw_swarm(self, screen: pygame.Surface) -> None:
        for agent in self.environment.swarm:
            if agent.vel.length() == 0:
                continue
        
            direction = agent.vel.normalize()
            
            angle = math.atan2(direction.y, direction.x)
            
            size = AGENT_RADIUS * 2
            tip = pygame.Vector2(agent.pos.x + math.cos(angle) * size, agent.pos.y + math.sin(angle) * size)
            left = pygame.Vector2(agent.pos.x + math.cos(angle + 2.5) * size, agent.pos.y + math.sin(angle + 2.5) * size)
            right = pygame.Vector2(agent.pos.x + math.cos(angle - 2.5) * size, agent.pos.y + math.sin(angle - 2.5) * size)
        
            pygame.draw.polygon(screen, AGENT_COLOR, [(tip.x, tip.y), (left.x, left.y), (right.x, right.y)])
    
    def draw_obstacles(self, screen: pygame.Surface) -> None:
        for obstacle_pos in self.environment.obstacle_positions:
            pygame.draw.circle(screen, OBSTACLE_COLOR, (int(obstacle_pos.x), int(obstacle_pos.y)), CIRCLE_OBSTACLE_RADIUS)
    
    def draw_wind_arrow(self, screen: pygame.Surface) -> None:
        start_pos = (50, 50)
        end_pos = (start_pos[0] + self.environment.wind_vec.x * WIND_ARROW_LENGTH, start_pos[1] + self.environment.wind_vec.y * WIND_ARROW_LENGTH)

        pygame.draw.line(screen, WIND_ARROW_COLOR, start_pos, end_pos, 1)            
    
        angle = math.atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])
        left_angle = angle - math.pi / 6
        right_angle = angle + math.pi / 6

        left = (end_pos[0] - WIND_ARROW_HEAD_SIZE * math.cos(left_angle), end_pos[1] - WIND_ARROW_HEAD_SIZE * math.sin(left_angle))
        right = (end_pos[0] - WIND_ARROW_HEAD_SIZE * math.cos(right_angle), end_pos[1] - WIND_ARROW_HEAD_SIZE * math.sin(right_angle))
    
        pygame.draw.polygon(screen, WIND_ARROW_COLOR, [end_pos, left, right])
    
    def draw_wind(self, screen: pygame.Surface) -> None:
        font = pygame.font.SysFont(None, 24)
        text = font.render(f"Wind Force: {self.environment.wind_strength:.1f}", True, WIND_FORCE_TEXT_COLOR)
        screen.blit(text, (10, 10))