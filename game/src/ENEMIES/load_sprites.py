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
        'damage': 0.5,
        'idle': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/BAT/17.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/BAT/18.png'),
        ]
    },
    'tree': {
        'scale': 1.0,
        'health': 5,
        'damage': 1,
        'idle': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/IDLE/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/IDLE/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/IDLE/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/IDLE/3.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/IDLE/4.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/IDLE/19.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/IDLE/20.png'),
        ],
        'move': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/RUN/5.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/RUN/6.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/RUN/7.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/RUN/8.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/RUN/9.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/RUN/10.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/RUN/12.png'),
        ],
        'attack': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/ATTACK/13.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/ATTACK/14.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/ATTACK/15.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/ATTACK/16.png'),
        ],
        'die': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/DIE/38.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EVIL_TREE/DIE/39.png'),
        ]
    }
}
