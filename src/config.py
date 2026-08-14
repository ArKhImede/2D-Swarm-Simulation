# Number of agents created at the beginning of the simulation.
NUM_AGENTS: int = 30

# Max. movement speed of an agent.
MAX_SPEED: int = 50

# Max. distance at which agents influence one another.
NEIGHBOUR_RADIUS: int = 50

# Radius used when drawing each agent.
AGENT_RADIUS: int = 5

# Size of pygame window.
SCREEN_WIDTH: int = 1080
SCREEN_HEIGHT: int = 720

# Time step used to update the simulation.
DT: float = 0.02

# Colors used by the simulation.
AGENT_COLOR: str = "#808F85"
WINDOW_COLOR: str = "#DCE0D9"
WIND_ARROW_COLOR = "#FFFFFF"
OBSTACLE_COLOR: str = "#31081F"
WIND_FORCE_TEXT_COLOR: str = "#FFFFFF"

# Range used to randomly initialize agent velocities.
MIN_RANDOM_VEL: int = -5
MAX_RANDOM_VEL: int = 5

# Obstacle configurations.
CIRCLE_OBSTACLE_RADIUS: int = 30
REPULSION_STRENGTH: float = 40

# Wind configuration.
WIND_FORCE_STRENGTH: float = 2.5
WIND_ARROW_LENGTH = 70
WIND_ARROW_HEAD_SIZE = 10
