"""
Module for handling loading of enemy sprites
author: Joshua Akangah
date: 7/9/20
"""

from .settings import *

enemy_animations = {
    'bat': {
        'scale': 1.0,
        'health': 1,
        'idle': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/BAT/17.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/BAT/18.png'),
        ]
    }
}
