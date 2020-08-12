"""
Module for creating game tiles for snow mountain biome
author: Joshua Akangah
date: 11/8/20
"""

from CONFIG.settings import *

# game map
game_map = [
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0'],
    ['1','1','1','1','1','1','1','1','1','1'],
    ['1','1','1','1','1','1','1','1','1','1'],
]

topTile = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets/TILES/IceTiles/Ice_1_16x16.png")), (80,60))
bottomTile = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets/TILES/IceTiles/Ice_15_16x16.png")), (80,60))
midTile = pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets/TILES/IceTiles/Ice_15_16x16.png")), (80,60))

class SnowBiomeTile():
    def __init__(self):
        self.topTile = topTile
        self.bottomTile = bottomTile
        self.midTile = midTile
        self.tile_rects = []

    def draw(self, display):
        
        self.y = 0

        for layer in game_map:
            self.x = 0
            for tile in layer:
                if tile == '1':
                    display.blit(self.topTile, (self.x*80, self.y*60))                    
                elif tile == '2':
                    display.blit(self.midTile, (self.x*80, self.y*60))
                if tile != '0':
                    self.tile_rects.append(pygame.Rect(self.x*80, self.y*60, 80, 60))
                self.x += 1
            self.y += 1