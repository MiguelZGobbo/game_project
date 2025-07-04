from code.Entity import Entity

class Opponent(Entity):
    def __init__(self, name: str, position: tuple, speed: float = None):
        super().__init__(name, position)
        self.speed = speed if speed is not None else 3
        self.rect.centery = position[1]

    def move(self, events=None):
        self.rect.centerx -= self.speed