# AI Rocket Lander

This repository contains a Python implementation of a Deep Q-Network (DQN), designed to solve the "LunarLander-v2" environment from OpenAI's Gym library. The DQN agent learns to land a spacecraft safely by interacting with the environment and refining its strategy based on the received rewards. This implementation showcases foundational techniques in reinforcement learning, such as experience replay and target network.

# Environment Overview

The Lunar Lander environment is a popular benchmark in reinforcement learning where the goal is to safely land a spacecraft on the moon. The agent must control the lander's engines to decelerate and adjust its position to land at a specific location with minimal fuel consumption. Successful landing is indicated by the lander coming to rest on the landing pad, which is always at coordinates (0,0).

- Observation Space: The state consists of eight variables, including the lander's position, velocity, angle, angular velocity, and two booleans indicating whether each leg is in contact with the ground.
- Actions: There are four discrete actions available: do nothing, fire left orientation engine, fire main engine, and fire right orientation engine.
- Rewards: The reward system penalizes fuel usage, moving away from the landing zone, and crashing. It rewards coming to rest on the landing pad and conserving fuel.


