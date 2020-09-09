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
    },
    'eye': {
        'scale': 1.0,
        'health': 10,
        'damage': 3,
        'idle': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/IDLE/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/IDLE/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/IDLE/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/IDLE/3.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/IDLE/4.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/IDLE/5.png'),
        ],
        'move': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/FLY/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/FLY/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/FLY/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/FLY/3.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/FLY/4.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/FLY/5.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/FLY/6.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/FLY/7.png'),
        ],
        'die': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/DIE/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/DIE/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/DIE/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/DIE/3.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/DIE/4.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/DIE/6.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/DIE/8.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/DIE/9.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/DIE/10.png'),
        ],
        'attack': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/ATTACK/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/ATTACK/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/ATTACK/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/ATTACK/3.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/ATTACK/4.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/ATTACK/5.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/ATTACK/6.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/ATTACK/7.png'),
        ],
        'damage': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/DAMAGE/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/DAMAGE/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/DAMAGE/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/EYE/DAMAGE/3.png'),
        ]
    },
    'goblin': {
        'scale': 1.0,
        'health': 20,
        'damage': 5,
        'idle': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/IDLE/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/IDLE/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/IDLE/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/IDLE/3.png'),
        ],
        'move': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/RUN/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/RUN/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/RUN/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/RUN/3.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/RUN/4.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/RUN/5.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/RUN/6.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/RUN/7.png'),
        ],
        'damage': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/DAMAGE/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/DAMAGE/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/DAMAGE/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/DAMAGE/3.png'),
        ],
        'attack': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/ATTACK/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/ATTACK/3.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/ATTACK/4.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/ATTACK/5.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/ATTACK/6.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/ATTACK/7.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/ATTACK/8.png'),
        ],
        'die': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/DIE/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/DIE/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/DIE/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/GOBLIN/DIE/3.png'),
        ]
    },
    'mushroom': {
        'scale': 1.0,
        'health': 20,
        'damage': 5,
        'idle': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/IDLE/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/IDLE/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/IDLE/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/IDLE/3.png'),
        ],
        'move': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/RUN/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/RUN/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/RUN/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/RUN/3.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/RUN/4.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/RUN/5.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/RUN/6.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/RUN/7.png'),
        ],
        'damage': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/DAMAGE/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/DAMAGE/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/DAMAGE/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/DAMAGE/3.png'),
        ],
        'attack': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/ATTACK/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/ATTACK/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/ATTACK/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/ATTACK/3.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/ATTACK/4.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/ATTACK/5.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/ATTACK/6.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/ATTACK/7.png'),
        ],
        'die': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/DIE/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/DIE/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/DIE/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/DIE/3.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/DIE/4.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/DIE/5.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/DIE/6.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/MUSHROOM/DIE/7.png'),
        ]
    },
    'skeleton': {
        'scale': 0.85,
        'health': 20,
        'damage': 5,
        'idle': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/IDLE/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/IDLE/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/IDLE/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/IDLE/3.png'),
        ],
        'move': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/RUN/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/RUN/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/RUN/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/RUN/3.png'),
        ],
        'damage': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/DAMAGE/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/DAMAGE/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/DAMAGE/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/DAMAGE/3.png'),
        ],
        'attack': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/ATTACK/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/ATTACK/3.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/ATTACK/4.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/ATTACK/9.png'),
        ],
        'die': [
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/DIE/0.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/DIE/1.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/DIE/2.png'),
            os.path.join(BASE_DIR, 'assets/ENEMIES/SKELETON/DIE/3.png'),
        ]
    }
}
