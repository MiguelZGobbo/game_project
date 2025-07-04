from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED[name]

    def move(self, events):
        self.rect.centerx -= self.speed
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH