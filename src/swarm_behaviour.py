import pygame
from config import *


class SwarmBehaviour:
    """
    Implements the basic flocking rules used by each agent.

    The three main flocking behaviors are:

    - Separation: agents avoid getting too close to one another.
    - Alignment: agents try to match the velocity of nearby agents.
    - Cohesion: agents try to move toward the center of nearby agents.
    """

    def __init__(self) -> None:
        # Relative importance of each flocking behavior.
        self.separation_weight: float = 1.5
        self.alignment_weight: float = 1.0
        self.cohesion_weight: float = 0.5

        # Max. allowed speed.
        self.max_speed: float = MAX_SPEED

        # Max. distance at which another agent is considered a neighbor.
        self.min_dist_to_neighbour = NEIGHBOUR_RADIUS

    def get_neighbors(self, swarm: list) -> list:
        """
        Return all agents located within the neighborhood radius.
        """

        neighbors = []

        for other in swarm:
            if (other != self) and (
                pygame.Vector2.distance_to(self.pos, other.pos)
                <= self.min_dist_to_neighbour
            ):
                neighbors.append(other)

        return neighbors

    def separation(self, swarm: list) -> pygame.Vector2:
        """
        Create a force that pushes the agent away from the nearby agents.
        Closer neighbors produce a stronger repulsive force.
        """

        sep_vec = pygame.Vector2(0, 0)
        neighbors = self.get_neighbors(swarm)

        for neighbor in neighbors:
            # Vector pointing away from the neighboring agent.
            diff = self.pos - neighbor.pos
            dist = diff.length()

            # Avoid normalizing a zero-length vector.
            if dist > 0:
                # Dividing by distance makes closer agents have more influence.
                sep_vec += diff.normalize() / dist

        if neighbors:
            return sep_vec * self.separation_weight
        return pygame.Vector2(0, 0)

    def alignment(self, swarm) -> pygame.Vector2:
        """
        Create a force that makes the agent match nearby velocities.
        """

        neighbors = self.get_neighbors(swarm)

        if not neighbors:
            return pygame.Vector2(0, 0)

        # Calculate the avg. velocity of all nearby agents.
        avg_vel_nearby_neighbours = sum(
            (neighbor.vel for neighbor in neighbors), pygame.Vector2(0, 0)
        ) / len(neighbors)

        # The desired change is the difference between the avg. velocity and the current agent's velocity.
        steering_vec = avg_vel_nearby_neighbours - self.vel

        if steering_vec.length() > 0:
            return steering_vec.normalize() * self.alignment_weight
        return pygame.Vector2(0, 0)

    def cohesion(self, swarm) -> pygame.Vector2:
        """
        Create a force that moves the agent toward nearby agents.
        """

        neighbors = self.get_neighbors(swarm)

        if not neighbors:
            return pygame.Vector2(0, 0)

        # Calculate the avg. position of nearby agents.
        avg_pos_neighbours = sum(
            (neighbor.pos for neighbor in neighbors), pygame.Vector2(0, 0)
        ) / len(neighbors)

        # Vector from the current agent to the local group center.
        vec_to_avg_center = avg_pos_neighbours - self.pos

        return vec_to_avg_center.normalize() * self.cohesion_weight

    def update_agent_pos(self, dt: float, swarm: list) -> None:
        """
        Update the agent's velocity and position for one simulation step.
        """

        # Combine the three flocking forces.
        steering = self.separation(swarm) + self.alignment(swarm) + self.cohesion(swarm)

        # Limit the total steering force.
        max_force = 0.5
        if steering.length() > max_force:
            steering.scale_to_length(max_force)

        # Update the agent's velocity using the steering force.
        self.vel += steering

        # Limit the agent's maximum speed.
        if self.vel.length() > self.max_speed:
            self.vel.scale_to_length(self.max_speed)

        # Update position using velocity and the time step.
        self.pos += self.vel * dt
