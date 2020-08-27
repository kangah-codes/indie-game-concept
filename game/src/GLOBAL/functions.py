"""
Global collision functions
author: Joshua Akangah
date: 12/8/20
"""

from CONFIG.settings import *

def collisionTest(rect, tiles):
    hitList = []
    for tile in tiles:
        if rect.colliderect(tile):
            hitList.append(tile)
    return hitList

def move(rect, movement, tiles):
    collision_types = {'top':False,'bottom':False,'right':False,'left':False}
    rect.x += movement[0]
    hit_list = collisionTest(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True

    rect.y += movement[1]
    hit_list = collisionTest(rect,tiles)

    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
            
    return rect, collision_types

    
# function for chunk generating in world
def generate_chunk(x, y):
    chunk_data = []
    clouds = []

    for y_pos in range(CHUNK_SIZE):
        for x_pos in range(CHUNK_SIZE):
            target_x = x * CHUNK_SIZE + x_pos
            target_y = y * CHUNK_SIZE + y_pos

            tile_type = 0
            
            # using perlin noise for random terrain generation
            height = int(noise.pnoise1(target_x*0.1, repeat=9999999) * 5)

            if target_y > (7 - height):
                tile_type = 2 # dirt
            elif target_y == 7 - height:
                tile_type = 1 # grass
            elif target_y == 7 - height - 1:
                if random.randint(1, 5) == 1:
                    # randomly place grass
                    tile_type = 3 
                elif random.randint(5, 20) == 6:
                    tile_type = 4
            if tile_type != 0:
                chunk_data.append([[target_x, target_y], tile_type])

    return chunk_data