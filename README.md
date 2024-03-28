# AI_rocket_lander

AI Agent solving the Lunar Lander as described in https://gymnasium.farama.org/environments/box2d/lunar_lander/

The Lunar Lander environment is a popular benchmark in reinforcement learning where the goal is to safely land a spacecraft on the moon. The agent must control the lander's engines to decelerate and adjust its position to land at a specific location with minimal fuel consumption. Successful landing is indicated by the lander coming to rest on the landing pad, which is always at coordinates (0,0).

# Environment Overview

- Observation Space: The state consists of eight variables, including the lander's position, velocity, angle, angular velocity, and two booleans indicating whether each leg is in contact with the ground.
- Actions: There are four discrete actions available: do nothing, fire left orientation engine, fire main engine, and fire right orientation engine.
- Rewards: The reward system penalizes fuel usage, moving away from the landing zone, and crashing. It rewards coming to rest on the landing pad and conserving fuel.

# Artificial Neural Network (ANN) Design and Architecture

- Input Layer: The input layer consists of neurons equal to the size of the observation space (8 neurons).
- Hidden Layers: Typically, one or two hidden layers with a variable number of neurons are used. The exact architecture can be determined through experimentation, but a common starting point is two hidden layers with 64 neurons each.
- Output Layer: The output layer has neurons corresponding to the number of actions (4 neurons). The output uses a softmax function to decide on the action to take.
