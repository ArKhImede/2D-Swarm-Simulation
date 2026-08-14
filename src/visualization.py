import pygame
from environment import Environment
from config import *
import math


class Visualization:
    """
    Draw the swarm, obstacles, wind arrow and wind information.
    """

    def __init__(self, environment: Environment) -> None:
        # Store the size of the simulation area.
        self.screen_width: int = SCREEN_WIDTH
        self.screen_height: int = SCREEN_HEIGHT

        # Keep a reference to the environment so that its data can be drawn.
        self.environment = environment

    def draw_swarm(self, screen: pygame.Surface) -> None:
        """
        Draw every agent as a triangle pointing in its direction of movement.
        """

        for agent in self.environment.swarm:
            # An agent without velocity has no direction to point toward.
            if agent.vel.length() == 0:
                continue

            # Convert velocity into a unit direction vector.
            direction = agent.vel.normalize()

            # Find the angle of movement in radians.
            angle = math.atan2(direction.y, direction.x)

            # Size of the triangular agent.
            size = AGENT_RADIUS * 2

            # Calculate the three triangle vertices.
            tip = pygame.Vector2(
                agent.pos.x + math.cos(angle) * size,
                agent.pos.y + math.sin(angle) * size,
            )
            left = pygame.Vector2(
                agent.pos.x + math.cos(angle + 2.5) * size,
                agent.pos.y + math.sin(angle + 2.5) * size,
            )
            right = pygame.Vector2(
                agent.pos.x + math.cos(angle - 2.5) * size,
                agent.pos.y + math.sin(angle - 2.5) * size,
            )

            # Draw the agent as a filled triangle.
            pygame.draw.polygon(
                screen,
                AGENT_COLOR,
                [(tip.x, tip.y), (left.x, left.y), (right.x, right.y)],
            )

    def draw_obstacles(self, screen: pygame.Surface) -> None:
        """
        Draw all circular obstacles.
        """

        for obstacle_pos in self.environment.obstacle_positions:
            pygame.draw.circle(
                screen,
                OBSTACLE_COLOR,
                (int(obstacle_pos.x), int(obstacle_pos.y)),
                CIRCLE_OBSTACLE_RADIUS,
            )

    def draw_wind_arrow(self, screen: pygame.Surface) -> None:
        """
        Draw an arrow showing the current wind direction.
        """

        # Starting point of the wind arrow.
        start_pos = (50, 50)

        # Calculate the endpoint from the wind direction and arrow length.
        end_pos = (
            start_pos[0] + self.environment.wind_vec.x * WIND_ARROW_LENGTH,
            start_pos[1] + self.environment.wind_vec.y * WIND_ARROW_LENGTH,
        )

        # Draw the main line of the arrow.
        pygame.draw.line(screen, WIND_ARROW_COLOR, start_pos, end_pos, 1)

        # Calculate the arrow's angle.
        angle = math.atan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])

        # The arrowhead consists of two lines angled away from the direction.
        left_angle = angle - math.pi / 6
        right_angle = angle + math.pi / 6

        left = (
            end_pos[0] - WIND_ARROW_HEAD_SIZE * math.cos(left_angle),
            end_pos[1] - WIND_ARROW_HEAD_SIZE * math.sin(left_angle),
        )
        right = (
            end_pos[0] - WIND_ARROW_HEAD_SIZE * math.cos(right_angle),
            end_pos[1] - WIND_ARROW_HEAD_SIZE * math.sin(right_angle),
        )

        # Draw the arrowhead as a triangle.
        pygame.draw.polygon(screen, WIND_ARROW_COLOR, [end_pos, left, right])

    def draw_wind(self, screen: pygame.Surface) -> None:
        """
        Display the current wind strength in the top-left corner.
        """

        # Create a font for the wind label.
        font = pygame.font.SysFont(None, 24)

        # Render the wind strength as text.
        text = font.render(
            f"Wind Force: {self.environment.wind_strength:.1f}",
            True,
            WIND_FORCE_TEXT_COLOR,
        )

        # Draw the text near the top-left corner.
        screen.blit(text, (10, 10))
