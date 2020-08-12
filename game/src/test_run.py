from CONFIG.game import *
from PLAYER.sprite import *
from ENTITIES.HEART.hearts import *
from WORLD.tiles import *

game = Game()

p = Player()
t = Tile('ice')

game.playerGroup.append(p)
game.spriteGroup.add(Heart(p))
game.tiles = t

game.run()