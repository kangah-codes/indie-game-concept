from CONFIG.game import *
from PLAYER.sprite import *
from ENTITIES.HEART.hearts import *
from WORLD.SNOW_MOUNTAINS.background import *
from WORLD.SNOW_MOUNTAINS.tiles import *

game = Game()

Background = SnowMountainBiome()

p = Player()

game.playerGroup.append(p)
game.spriteGroup.add(Heart(p))
game.tiles.append(SnowBiomeTile())
#game.background = Background

game.run()

# p = Player(game.space)

# from ENTITIES.HEART.hearts import *