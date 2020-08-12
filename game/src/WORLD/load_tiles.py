"""
Module for loading game tiles
author: Joshua Akangah
date: 12/8/20
"""

from CONFIG.settings import *

snow_mountain_tiles = {
    'top': [
        pygame.image.load((os.path.join(BASE_DIR, 'assets/TILES/IceTiles/Ice_9_16x16.png'))), 
        pygame.image.load((os.path.join(BASE_DIR, 'assets/TILES/IceTiles/Ice_10_16x16.png'))), 
    ],
    'middle': pygame.image.load((os.path.join(BASE_DIR, 'assets/TILES/dirt.png'))),
}   