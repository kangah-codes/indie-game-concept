"""
Parralax background module 
author: Joshua Akangah
date: 15/8/20
"""

from CONFIG.settings import *

# forest biome
forest_background = {
    1: pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, 'assets/BIOMES/FOREST/Layer_0010_1.png')), DISPLAY_SIZE),
    2: pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, 'assets/BIOMES/FOREST/Layer_0009_2.png')), DISPLAY_SIZE),
    3: pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, 'assets/BIOMES/FOREST/Layer_0008_3.png')), DISPLAY_SIZE),
    4: pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, 'assets/BIOMES/FOREST/Layer_0006_4.png')), DISPLAY_SIZE),
    5: pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, 'assets/BIOMES/FOREST/Layer_0005_5.png')), DISPLAY_SIZE),
    6: pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, 'assets/BIOMES/FOREST/Layer_0003_6.png')), DISPLAY_SIZE),
    7: pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, 'assets/BIOMES/FOREST/Layer_0000_9.png')), DISPLAY_SIZE),
    8: pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, 'assets/BIOMES/FOREST/Layer_0002_7.png')), DISPLAY_SIZE),
}

forest_tiles = {
    1: pygame.image.load(os.path.join(BASE_DIR, 'assets/TILES/SwampTiles/Grass_2_16x16.png')), # topGrass
    2: pygame.image.load(os.path.join(BASE_DIR, 'assets/TILES/SwampTiles/Bramble_1_16x16.png')), # dirt
    3: pygame.image.load(os.path.join(BASE_DIR, 'assets/plant.png')), # grass
    4: pygame.image.load(os.path.join(BASE_DIR, 'assets/BIOMES/TREES/apple.png')), # dead tree
}

# snow biome
snow_mountains = {
    1: pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, 'assets/BIOMES/SNOW_MOUNTAINS/mountains_flip.png')), DISPLAY_SIZE)
}

snow_tiles = {
    1: pygame.image.load(os.path.join(BASE_DIR, 'assets/TILES/IceTiles/Ice_1_16x16.png')), # topGrass
    2: pygame.image.load(os.path.join(BASE_DIR, 'assets/TILES/IceTiles/Ice_17_16x16.png')), # dirt
    3: pygame.image.load(os.path.join(BASE_DIR, 'assets/plant.png')), # grass
    4: pygame.image.load(os.path.join(BASE_DIR, 'assets/BIOMES/TREES/dead_tree.png')), # dead tree
}

clouds = {
    1: pygame.image.load(os.path.join(BASE_DIR, 'assets/BIOMES/SNOW_MOUNTAINS/0.png'))
}