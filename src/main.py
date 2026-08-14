import pygame
from agent import Agent
from environment import Environment
from visualization import Visualization
from config import *


def main():
    """Create and run the swarm simulation."""

    # Initialize all Pygame modules.
    pygame.init()

    # Create the initial swarm of agents.
    swarm = [Agent() for _ in range(NUM_AGENTS)]

    # Create the environment and visualization objects.
    environment = Environment(swarm)
    vis = Visualization(environment)

    # Create the application window.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("2D Swarm Simulation")

    # Clock is used to control the simulation frame rate.
    clock = pygame.time.Clock()

    running = True
    while running:
        # Process user and system events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Add a new obstacle when the left mouse button is clicked.
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
                    environment.obstacle_positions.append(mouse_pos)

            # Increase or decrease wind strength using the arrow keys.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    environment.wind_strength += 0.5
                elif event.key == pygame.K_DOWN:
                    environment.wind_strength = max(0, environment.wind_strength - 0.5)

        # Update the movement and swarm behavior of every agent.
        for agent in swarm:
            agent.update_agent_pos(DT, swarm)

        # Apply environmental forces after the swarm behavior.
        environment.apply_obstacle_force()
        environment.apply_wind_force()
        environment.handle_boundaries()

        screen.fill(WINDOW_COLOR)

        # Draw all simulation elements.
        vis.draw_swarm(screen)
        vis.draw_obstacles(screen)
        vis.draw_wind_arrow(screen)
        vis.draw_wind(screen)

        pygame.display.flip()
        clock.tick(int(1 / DT))

    pygame.quit()


if __name__ == "__main__":
    main()
