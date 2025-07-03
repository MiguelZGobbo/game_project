import random
from Const import WIN_WIDTH, WIN_HEIGHT, TRACK_MIDDLE, TRACK_TOP, TRACK_DOWN, ENTITY_SPEED, MENU_OPTION
from code.Background import Background
from code.Player import Player
from code.Enemy import Enemy

class EntityFactory:
    _new_wave_generated = False
    _base_enemy_speed = ENTITY_SPEED['Enemy1']  # Velocidade base inicial
    _speed_increment = 0.5  # Incremento padrão para Fácil
    _current_game_mode = None  # Rastreia o modo de jogo atual

    @staticmethod
    def get_entity(entity_name: str, position=(0,0), current_entities=None, game_mode=None):
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
                # Define velocidade inicial e incremento apenas se o game_mode mudou ou é a primeira onda
                if game_mode != EntityFactory._current_game_mode:
                    EntityFactory._base_enemy_speed = ENTITY_SPEED['Enemy1']
                    EntityFactory._speed_increment = 0.5  # Padrão para Fácil
                    if game_mode == MENU_OPTION[1]:  # 'JOGAR MODO MÉDIO'
                        EntityFactory._base_enemy_speed += 1.0  # 3 + 1 = 4.0
                        EntityFactory._speed_increment = 0.65
                    elif game_mode == MENU_OPTION[2]:  # 'JOGAR MODO DIFÍCIL'
                        EntityFactory._base_enemy_speed += 1.5  # 3 + 1.5 = 4.5
                        EntityFactory._speed_increment = 0.80
                    EntityFactory._current_game_mode = game_mode
                    print(f"[EntityFactory] Novo modo iniciado - Modo: {game_mode}, Velocidade inicial: {EntityFactory._base_enemy_speed}")

                # Verifica se deve gerar nova onda de inimigos
                should_generate_enemies = (
                    current_entities is not None and
                    not any(isinstance(ent, Enemy) for ent in current_entities) and
                    not EntityFactory._new_wave_generated
                )

                if should_generate_enemies:
                    tracker_positions = [TRACK_TOP, TRACK_MIDDLE, TRACK_DOWN]
                    pistas = random.sample(tracker_positions, 2)

                    inimigos = []
                    x_pos = WIN_WIDTH + 10
                    for y_pos in pistas:
                        inimigo = Enemy('Enemy1', (x_pos, y_pos), speed=EntityFactory._base_enemy_speed)
                        inimigos.append(inimigo)
                    EntityFactory._new_wave_generated = True
                    print(f"[EntityFactory] Nova onda criada - Modo: {game_mode}, Velocidade inicial: {EntityFactory._base_enemy_speed}")
                    return inimigos
                
                # Reset da flag se não houver mais inimigos
                if current_entities is not None and not any(isinstance(ent, Enemy) for ent in current_entities):
                    EntityFactory._new_wave_generated = False
                
                return []