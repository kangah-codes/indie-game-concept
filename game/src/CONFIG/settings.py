"""
Main game settings module
author: Joshua Akangah
date: 10/9/20
"""

import pygame
import os
import time
import random

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
FPS = 60
CLOCK = pygame.time.Clock()

# screen sizes
info = pygame.display.Info() # You have to call this before pygame.display.set_mode()
screen_width, screen_height = info.current_w, info.current_h
window_width, window_height = 600, 400

CHUNK_SIZE = 16