"""
	Main game settings module
	author: Joshua Akangah
    date: 10/9/20
"""

import pygame
import os
# import pymunk
# import pymunk.pygame_util
import math

#
# print(pymunk.pygame_util.positive_y_is_up)
# pymunk.pygame_util.positive_y_is_up = False
# print(pymunk.pygame_util.positive_y_is_up)
# base project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# GLOBAL VARS
FPS = 60
CLOCK = pygame.time.Clock()

# player deltatime update
DT = FPS * 0.0001
