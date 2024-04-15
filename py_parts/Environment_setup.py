# Setting up the environment

import gymnasium as gym
env = gym.make("LunarLander-v2")
state_shape = env.observation_space.shape
state_size = env.observation_space.shape[0]
number_actions = env.action_space.n
