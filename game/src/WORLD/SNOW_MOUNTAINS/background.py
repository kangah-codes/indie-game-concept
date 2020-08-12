"""
Module for snow mountains
author: Joshua Akangah
date: 11/8/20
"""

from CONFIG.settings import *
from ..BACKGROUND.parallax import *

class SnowMountainBiome():
    def __init__(self):
        self.background = ParallaxSurface((800, 600), pygame.RLEACCEL)
        self.background.add(os.path.join(BASE_DIR, "assets/BIOMES/SNOW_MOUNTAINS/sky_lightened.png"), 2, None, True, 800, 600)
        self.background.add(os.path.join(BASE_DIR, "assets/BIOMES/SNOW_MOUNTAINS/clouds_bg.png"), 2.3, None, True, 800, 600)
        
        self.background.add(os.path.join(BASE_DIR, "assets/BIOMES/SNOW_MOUNTAINS/glacial_mountains_lightened.png"), 4, None, True, 800, 600)
        self.background.add(os.path.join(BASE_DIR, "assets/BIOMES/SNOW_MOUNTAINS/mountains_flip.png"), 2, None, True, 800, 600)
        self.background.add(os.path.join(BASE_DIR, "assets/BIOMES/SNOW_MOUNTAINS/clouds_mg_3.png"), 3, None, True, 800, 600)
        self.background.add(os.path.join(BASE_DIR, "assets/BIOMES/SNOW_MOUNTAINS/clouds_mg_2.png"), 4, None, True, 800, 600)
        self.background.add(os.path.join(BASE_DIR, "assets/BIOMES/SNOW_MOUNTAINS/clouds_mg_1.png"), 5, None, True, 800, 600)
        self.background.add(os.path.join(BASE_DIR, "assets/BIOMES/SNOW_MOUNTAINS/cloud_lonely.png"), 1, None, True, 800, 600)
        
        # self.background.add(os.path.join(BASE_DIR, "assets/BIOMES/SNOW_MOUNTAINS/sky_lightened.png"), 7)
        # self.background.add(os.path.join(BASE_DIR, "assets/BIOMES/SNOW_MOUNTAINS/sky_lightened.png"), 8)
        # self.background.add(os.path.join(BASE_DIR, "assets/BIOMES/SNOW_MOUNTAINS/sky_lightened.png"), 9)
    
    def update(self, speed):
        self.background.scroll(speed, orientation='horizontal')