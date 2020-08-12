"""
Tile manager for game world
author: Joshua Akangah
date: 12/8/20
"""

from CONFIG.settings import *
from .load_tiles import *

class Tile():
    def __init__(self, typeOF):
        self.typeOf = typeOF
        self.y = 0
        self.x = 0
        self.rects = []
        self.topImage = random.choice(snow_mountain_tiles.get('top'))
        self.middleImage = snow_mountain_tiles.get('middle')

        self.tileIndex = {
            1: self.topImage,
            2: self.middleImage,
            3: self.middleImage,
        }

    def draw(self, map, display):
        for tile in map:
            if tile[1] == 1:
                # top
                display.blit(self.topImage, (tile[0][0]*16, tile[0][1]*16))
            elif tile == 2:
                display.blit(self.middleImage, (tile[0][0]*16, tile[0][1]*16))
            if tile != 0:
                self.rects.append(pygame.Rect(tile[0][0]*16, tile[0][1]*16, 16, 16))