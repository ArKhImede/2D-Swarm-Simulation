# 🦟 2D Swarm Simulation

A 2D boids-style swarm simulation built with `pygame`. Agents move according to classic flocking rules (separation, alignment, cohesion) while reacting to obstacles, wind, and screen boundaries in real time.

## ⚙️ Features

- **Flocking behaviour** — each agent steers based on nearby neighbours using separation, alignment, and cohesion forces
- **Obstacles** — static circular obstacles repel nearby agents; click anywhere on the screen to add new obstacles
- **Wind force** — a global wind vector pushes the whole swarm; strength is adjustable at runtime
- **Boundary handling** — agents are steered back into view when they approach the edges of the screen
- **Simple visualization** — agents are drawn as triangles oriented along their velocity, with an on-screen wind indicator

## 🕹️ Demo Controls

| Input | Action |
|---|---|
| `Left Click` | Add a new obstacle at the mouse position |
| `Up Arrow` | Increase wind strength |
| `Down Arrow` | Decrease wind strength |
| Close window | Quit the simulation |

## 🗂️ Project Structure

```
├── main.py             # Entry point — game loop, event handling
├── agent.py             # Agent class (position, velocity, color)
├── swarm_behaviour.py    # Flocking logic: separation, alignment, cohesion
├── environment.py        # Obstacles, wind, and boundary forces
├── visualization.py      # Rendering agents, obstacles, and wind arrow
├── utils.py               # Helper functions (random position/velocity)
└── config.py              # All tunable constants (speeds, colors, sizes, etc.)
```

## Installation

```https://github.com/ArKhImede/2D-Swarm-Simulation.git```

```cd 2D-Swarm-Simulation```

```pip install pygame```

## Usage

Run the simulation with:

```python main.py```

A window will open showing the swarm. Click to place obstacles and use the arrow keys to adjust wind strength while the simulation runs.

## Configuration

All simulation parameters live in `config.py`, including:

- `NUM_AGENTS`, `MAX_SPEED`, `NEIGHBOUR_RADIUS` — swarm size and movement
- `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `DT` — window size and simulation timestep
- `CIRCLE_OBSTACLE_RADIUS`, `REPULSION_STRENGTH` — obstacle behaviour
- `WIND_FORCE_STRENGTH` — initial wind strength
- Color settings for agents, obstacles, and background

Tweak these values to experiment with different swarm dynamics.

## How It Works

Each `Agent` inherits flocking behaviour from `SwarmBehaviour`, which computes three steering vectors based on nearby neighbours (within `NEIGHBOUR_RADIUS`):

1. **Separation** — steers away from neighbours that are too close
2. **Alignment** — steers toward the average heading of neighbours
3. **Cohesion** — steers toward the average position of neighbours

These are combined, capped by a maximum steering force, and applied to each agent's velocity every frame. The `Environment` class then layers in obstacle repulsion, wind, and boundary corrections before agents are redrawn by `Visualization`.

## 🎥 Video

Here is a video showing the simulation at work:

https://github.com/user-attachments/assets/76be975f-c97d-4ae0-bace-89c42b540fbd
