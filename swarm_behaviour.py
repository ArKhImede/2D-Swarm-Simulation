import pygame
from config import *

class SwarmBehaviour:
    
    def __init__(self) -> None:
        self.separation_weight: float = 1.5
        self.alignment_weight: float = 1.0
        self.cohesion_weight: float = 0.5
        self.max_speed: float = MAX_SPEED
        self.min_dist_to_neighbour = NEIGHBOUR_RADIUS
    
    def get_neighbors(self, swarm: list) -> list:
        neighbors = []
        
        for other in swarm:
            if (other != self) and (pygame.Vector2.distance_to(self.pos, other.pos) <= self.min_dist_to_neighbour):
                neighbors.append(other)
        
        return neighbors
    
    def separation(self, swarm: list) -> pygame.Vector2:
        sep_vec = pygame.Vector2(0, 0)
        neighbors = self.get_neighbors(swarm)
        
        for neighbor in neighbors:
            diff = self.pos - neighbor.pos
            dist = diff.length()
        
            if dist > 0:
                sep_vec += diff.normalize() / dist
        
        if neighbors:
            return sep_vec * self.separation_weight
        return pygame.Vector2(0, 0)
        
    def alignment(self, swarm) -> pygame.Vector2:
        neighbors = self.get_neighbors(swarm)

        if not neighbors:
            return pygame.Vector2(0, 0)
        
        avg_vel_nearby_neighbours = sum((neighbor.vel for neighbor in neighbors), pygame.Vector2(0, 0)) / len(neighbors)
        steering_vec = (avg_vel_nearby_neighbours - self.vel) 
        
        if steering_vec.length() > 0:
            return steering_vec.normalize() * self.alignment_weight
        return pygame.Vector2(0, 0)
        
    def cohesion(self, swarm) -> pygame.Vector2:
        neighbors = self.get_neighbors(swarm)
        
        if not neighbors:
            return pygame.Vector2(0, 0)
        
        avg_pos_neighbours = sum((neighbor.pos for neighbor in neighbors), pygame.Vector2(0, 0)) / len(neighbors)
        vec_to_avg_center = avg_pos_neighbours - self.pos
        return vec_to_avg_center.normalize() * self.cohesion_weight
    
    def update_agent_pos(self, dt: float, swarm: list) -> None:
        steering = (self.separation(swarm) + self.alignment(swarm) + self.cohesion(swarm))
        
        max_force = 0.5
        if steering.length() > max_force:
            steering.scale_to_length(max_force)
        
        self.vel += steering
        
        if self.vel.length() > self.max_speed:
            self.vel.scale_to_length(self.max_speed)
        
        self.pos += self.vel * dt