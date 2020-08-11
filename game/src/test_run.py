from CONFIG.game import *
from PLAYER.sprite import *
from ENTITIES.HEART.hearts import *

game = Game()

p = Player()

game.playerGroup.append(p)
game.spriteGroup.add(Heart(p))

game.run()

# p = Player(game.space)

# from ENTITIES.HEART.hearts import *