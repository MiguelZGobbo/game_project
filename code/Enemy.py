from code.Entity import Entity
from Const import ENTITY_SPEED, WIN_WIDTH

class Enemy(Entity):
    
    def __init__(self, name: str, position: tuple, speed: float = None):
        super().__init__(name, position)
        self.speed = speed if speed is not None else ENTITY_SPEED[name]  # Usa velocidade fornecida ou padrão

    def move(self, events=None):
        self.rect.centerx -= self.speed  # Move o inimigo para a esquerda