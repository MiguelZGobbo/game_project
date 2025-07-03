from code.Entity import Entity
from Const import ENTITY_SPEED, WIN_WIDTH

class Enemy(Entity):
    
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED[self.name]  # Velocidade inicial baseada na constante
        self.speed_increment = 0.01  # Incremento de velocidade por frame

    def move(self, events=None):
        self.speed += self.speed_increment  # Aumenta a velocidade
        self.rect.centerx -= self.speed  # Move o inimigo para a esquerda