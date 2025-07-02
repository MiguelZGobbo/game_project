from code.Background import Background
from Const import WIN_WIDTH

class EntityFactory:

    def __init__(self):
        pass
    
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'LevelBg':
                lista_bg = []
                for i in range(2):
                    lista_bg.append(Background(f'LevelBg{i}', (0,0)))
                    lista_bg.append(Background(f'LevelBg{i}', (WIN_WIDTH,0)))
                return lista_bg