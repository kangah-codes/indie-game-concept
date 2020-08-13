"""
Main game settings module
author: Joshua Akangah
date: 10/9/20
"""

import pygame
import os
import time
import random
import sys
import noise

from pygame.locals import *

os.environ['SDL_VIDEO_CENTERED'] = '1'
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
FPS = 90
CLOCK = pygame.time.Clock()

# screen sizes
SCREEN_SIZE = (600, 400)
DISPLAY_SIZE = (SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2)

CHUNK_SIZE = 8