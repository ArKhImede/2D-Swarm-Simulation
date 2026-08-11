import pygame
from agent import Agent
from environment import Environment
from visualization import Visualization
from config import *


def main():
    pygame.init()

    swarm = [Agent() for _ in range(NUM_AGENTS)]

    environment = Environment(swarm)
    vis = Visualization(environment)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("2D Swarm Simulation")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
                    environment.obstacle_positions.append(mouse_pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    environment.wind_strength += 0.5
                elif event.key == pygame.K_DOWN:
                    environment.wind_strength = max(0, environment.wind_strength - 0.5)

        for agent in swarm:
            agent.update_agent_pos(DT, swarm)

        environment.apply_obstacle_force()
        environment.apply_wind_force()
        environment.handle_boundaries()

        screen.fill(WINDOW_COLOR)

        vis.draw_swarm(screen)
        vis.draw_obstacles(screen)
        vis.draw_wind_arrow(screen)
        vis.draw_wind(screen)

        pygame.display.flip()
        clock.tick(int(1 / DT))

    pygame.quit()


if __name__ == "__main__":
    main()
