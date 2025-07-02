import random

from Const import WIN_WIDTH, WIN_HEIGHT, TRACK_MIDDLE, TRACK_TOP, TRACK_DOWN
from code.Background import Background
from code.Player import Player
from code.Enemy import Enemy


class EntityFactory:

    def __init__(self):
        pass
    
    @staticmethod
    def get_entity(entity_name: str, position=(0,0), current_entites = None):
        match entity_name:
            case 'LevelBg':
                lista_bg = []
                for i in range(2):
                    lista_bg.append(Background(f'LevelBg{i}', (0,0)))
                    lista_bg.append(Background(f'LevelBg{i}', (WIN_WIDTH,0)))
                return lista_bg
            
            case 'Player1':
                return Player('Player1', (20, TRACK_MIDDLE))
            
            case 'Enemy1':
                tracker_positions = [TRACK_TOP, TRACK_MIDDLE, TRACK_DOWN]
                # Escolhe dois índices aleatórios distintos para a dupla inicial
                pista_indices = [random.randint(0, 2), random.randint(0, 2)]
                # Garante que os índices sejam diferentes
                while pista_indices[0] == pista_indices[1]:
                    pista_indices[1] = random.randint(0, 2)
                inimigos = []
                x_pos = WIN_WIDTH + 10  # Posição horizontal fixa
                for pista_index in pista_indices:
                    y_pos = tracker_positions[pista_index]
                    inimigo = Enemy('Enemy1', (x_pos, y_pos))
                    inimigos.append(inimigo)
                return inimigos
