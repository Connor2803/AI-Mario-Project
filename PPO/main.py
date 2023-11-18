# ALEX HAWKING 2023
# 23354512

# IMPORTANT depending on your device you may need to change the device set at the top of src/agent

#######################
# Set saves directory #
#######################

# Required file structure, create folders beforehand
# ├── Mario/
# │ ├── main.py
# │ ├── model/
# │ | ├── checkpoints/


saves_directory = "./model"

###############################
# Hyper parameters for tuning #
###############################

# Discount rate
gamma = 0.95
# Advantage
lamda = 0.95
# Batch size
batch_size = 4096
# Mini batch size = batch_size / divisor
divisor = 4
# Clip range
epilson = 0.2
# Epochs
epochs = 30
# Agent and critic learning rates
a_lr = 0.00025
c_lr = 0.001

# Save interval (saves model and writes to csv every x episodes)
interval = 10

#############
# Rendering #
#############

# Can disable showing mario to increase training speed
show_game = False

#############
# Run modes #
#############

# Set to false if you just want to run the current policy without updating it
train = True

# Set to start if episode (if left at 0 it will just go to whatever the most recent episode is)
start = 0

# Show output in console
verbose = True

##################################################################################

import gym
from gym.wrappers import FrameStack
from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from src.preprocess import SkipFrame, GrayScaleObservation, ResizeObservation
from src.agent import Agent
import os
from src.utils import load_checkpoint

# Set up environment for pre-processing
if show_game:
    env = gym.make('SuperMarioBros-v0', apply_api_compatibility=True, render_mode="human")
else:
    env = gym.make('SuperMarioBros-v0', apply_api_compatibility=True)
env = JoypadSpace(env, [["right"], ["right", "A"]])
env = SkipFrame(env, skip=4)
env = GrayScaleObservation(env)
env = ResizeObservation(env, shape=84)
env = FrameStack(env, num_stack=4)

PPO_agent = Agent(env, saves_directory, gamma, lamda, epilson, epochs, divisor, interval, batch_size, a_lr, c_lr, show_game, verbose)

# Check that saves folder exists
load_checkpoint(saves_directory, PPO_agent, start)

# Continually run until stopped (ctrl + c)
if train:        
    while True:
        PPO_agent.train(PPO_agent.sample())
else:
    while True:
        PPO_agent.sample()