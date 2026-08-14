import pygame
from config import *


class Environment:
    """
    Controls external forces and environmental elements.

    The environment is responsible for:
    - Keeping agents inside the window
    - Applying obstacle repulsion
    - Applying wind
    - Storing obstacle positions
    """

    def __init__(self, swarm: list) -> None:
        # Store the dimensions of the simulation area.
        self.screen_width: int = SCREEN_WIDTH
        self.screen_height: int = SCREEN_HEIGHT

        # Store a reference to the list of agents.
        self.swarm: list = swarm

        # Initial obstacle positions.
        self.obstacle_positions = [
            pygame.Vector2(200, 200),
            pygame.Vector2(500, 300),
            pygame.Vector2(800, 600),
        ]

        # Wind direction and strength.
        # Vector (1, 0) means the wind moves from left to right.
        self.wind_vec = pygame.Vector2(1, 0)
        self.wind_strength = WIND_FORCE_STRENGTH

    def handle_boundaries(self) -> None:
        """
        Steers agents away from the edges of the screen.

        A soft boundary is used instead of immediately bouncing agents.
        The closer an agent is to an edge, the stronger the correction.
        """

        # Distance from the edge at which boundary steering begins.
        margin = 100

        # Strength of the steering force toward the center.
        turn_stregth = 1.5

        # Prevent the correction force from becoming too large.
        max_correction = 3.0

        for agent in self.swarm:
            # Start with no boundary force.
            steer = pygame.Vector2(0, 0)

            # Apply a force toward the right when near the left edge.
            if agent.pos.x < margin:
                strength = (1 - agent.pos.x / margin) * turn_stregth
                steer.x += min(strength, max_correction)

            # Apply a force toward the left when near the right edge.
            elif agent.pos.x > self.screen_width - margin:
                strength = (
                    1 - (self.screen_width - agent.pos.x) / margin
                ) * turn_stregth
                steer.x -= min(strength, max_correction)

            # Apply a force downward when near the top edge.
            if agent.pos.y < margin:
                strength = (1 - agent.pos.y / margin) * turn_stregth
                steer.y += min(strength, max_correction)

            # Apply a force upward when near the bottom edge.
            elif agent.pos.y > self.screen_height - margin:
                strength = (
                    1 - (self.screen_height - agent.pos.y) / margin
                ) * turn_stregth
                steer.y -= min(strength, max_correction)

            # Add the boundary steering force to the agent's velocity.
            agent.vel += steer

            # Clamp the agent's position so it remains inside the screen.
            agent.pos.x = max(0, min(self.screen_width, agent.pos.x))
            agent.pos.y = max(0, min(self.screen_height, agent.pos.y))

    def apply_obstacle_force(self) -> None:
        """
        Applies a repulsive force when an agent approaches an obstacle.
        """

        for agent in self.swarm:
            for obstacle_pos in self.obstacle_positions:
                # Vector pointing from the obstacle to the agent.
                dir_vec = agent.pos - obstacle_pos

                # Distance between the agent and the obstacle.
                distance = dir_vec.length()

                # Agents begin to feel the obstacle before touching it.
                interaction_radius = CIRCLE_OBSTACLE_RADIUS + 100

                # Only apply a force inside the interaction radius.
                # The distance check also prevents normalization of a zero vector.
                if 0 < distance < interaction_radius:
                    # Convert the direction into a unit vector.
                    dir_vec = dir_vec.normalize()

                    # Repulsion is strongest near the obstacle and decreases
                    # as the agent moves farther away.
                    strength = REPULSION_STRENGTH * (1 - distance / interaction_radius)

                    # Calculate the repulsion force.
                    force_vec = dir_vec * strength

                    # Apply the force using the simulation time step.
                    agent.vel += force_vec * DT

    def apply_wind_force(self) -> None:
        """
        Applies the wind foce to every agent.
        """

        for agent in self.swarm:
            # Wind direction multiplied by wind strength and time step.
            agent.vel += self.wind_vec * self.wind_strength * DT
