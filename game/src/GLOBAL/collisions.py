"""
Global collision functions
author: Joshua Akangah
date: 12/8/20
"""

def collision_test(object_1, object_list):
    collision_list = []
    for obj in object_list:
        if obj.colliderect(object_1):
            collision_list.append(obj)
    return collision_list