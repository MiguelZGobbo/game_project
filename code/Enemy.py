from code.Entity import Entity
from Const import ENTITY_SPEED, WIN_WIDTH

class Enemy(Entity):
    
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, events=None):
        self.rect.centerx -= ENTITY_SPEED[self.name]
    # NÃO reposiciona mais — deixa ele sair da tela para poder ser removido no Level
