"""
Settings mpdule for heart entity
author: Joshua Akangah
date: 11/8/20
"""

from CONFIG.settings import *

images = [
	pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets/EFFECTS/HEART/0.png")), (20, 18)),
	pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets/EFFECTS/HEART/1.png")), (20, 18)),
	pygame.transform.scale(pygame.image.load(os.path.join(BASE_DIR, "assets/EFFECTS/HEART/2.png")), (20, 18)),
]