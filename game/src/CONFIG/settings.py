"""
	Main game settings module
	author: Joshua Akangah
    date: 10/9/20
"""

import pygame
import os
pygame.init()

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
