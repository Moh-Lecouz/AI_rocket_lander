# AI Rocket Lander

This repository contains a Python implementation of a Deep Q-Network (DQN), designed to solve the "LunarLander-v2" environment from OpenAI's Gym library. The DQN agent learns to land a spacecraft safely by interacting with the environment and refining its strategy based on the received rewards. This implementation showcases foundational techniques in reinforcement learning, such as experience replay and target network.

# Environment Overview

The Lunar Lander environment is a popular benchmark in reinforcement learning where the goal is to safely land a spacecraft on the moon. The agent must control the lander's engines to decelerate and adjust its position to land at a specific location with minimal fuel consumption. Successful landing is indicated by the lander coming to rest on the landing pad, which is always at coordinates (0,0).

- Observation Space: The state consists of eight variables, including the lander's position, velocity, angle, angular velocity, and two booleans indicating whether each leg is in contact with the ground.
- Actions: There are four discrete actions available: do nothing, fire left orientation engine, fire main engine, and fire right orientation engine.
- Rewards: The reward system penalizes fuel usage, moving away from the landing zone, and crashing. It rewards coming to rest on the landing pad and conserving fuel.

# Requirements

- Python 3.x
- numpy
- torch (PyTorch)
- gymnasium (formerly gym)
- imageio (for rendering videos)

# Setting Up the Environment

Ensure all dependencies are installed using `pip`:
```bash
pip install torch numpy gymnasium "gymnasium[atari, accept-rom-license]" gymnasium[box2d] imageio
apt-get install -y swig
```

# Running the DQN Agent

To start training the agent, simply run the script:
```bash
python AI_Agent.py
```

# Structure

The main components of this implementation are as follows:

- Neural Network Architecture (neural_network): Defines the model used by both the local and target Q-networks. It consists of a simple feedforward neural network with three fully connected layers.

- Replay Memory (ReplayMemory): Implements the experience replay mechanism, allowing the agent to learn from past experiences stored in a buffer to break the correlation between consecutive learning samples.

- Agent (Agent): Encapsulates the decision-making logic, including interacting with the environment (act), storing experiences (step), and learning from minibatches of experiences (learn and soft_update).

- Training Loop: Runs episodes of environment interaction, during which the agent selects actions, processes the outcomes, and updates its knowledge.

- Video Rendering: Demonstrates the agent's performance by generating a video of a complete episode after training.

# Usage

1. Setup Environment: Ensure all required libraries are installed.

2. Run Training: Execute the script to train the agent. Training parameters such as the number of episodes, discount factor, and epsilon values for exploration can be adjusted at the beginning of the training loop section.

3. Monitor Progress: The script prints out the average score every 100 episodes. Training continues until the average score exceeds 200 points over 100 consecutive episodes, or until the maximum number of episodes is reached.

4. Visualize Performance: After training, a video of the agent's performance in the environment can be generated and displayed.

# Code Overview

## Model Definition
The neural network is defined using PyTorch's nn.Module. It takes the environment's state as input and outputs action values for each possible action. The architecture is simple yet effective for the Lunar Lander environment.

## Experience Replay
The ReplayMemory class is used to store and sample experiences. This mechanism is crucial for stabilizing the learning process by providing a diverse set of experiences for training the network.

## Agent Logic
The Agent class is the heart of the implementation. It includes methods for selecting actions (act), storing experiences (step), and learning from them (learn). It utilizes two networks (local and target) to estimate and update Q-values, employing a technique known as Fixed Q-Targets to stabilize training.

## Training and Evaluation
The training loop iterates over a specified number of episodes, interacting with the environment and optimizing the agent's policy. Post-training, the agent's performance can be visualized through a rendered video, showcasing the learned landing strategy.
