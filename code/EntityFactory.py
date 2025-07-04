import random
from code.Const import WIN_WIDTH, TRACK_MIDDLE, TRACK_TOP, TRACK_DOWN, ENTITY_SPEED, MENU_OPTION
from code.Background import Background
from code.Player import Player
from code.Opponent import Opponent

class EntityFactory:
    new_wave_generated = False
    base_opponent_speed = ENTITY_SPEED['Opponent1']
    speed_increment = 0.5
    current_game_mode = None

    @staticmethod
    def get_entity(entity_name: str, current_entities=None, game_mode=None):
        match entity_name:
            case 'LevelBg':
                background_list = []
                for i in range(2):
                    background_list.append(Background(f'LevelBg{i}', (0,0)))
                    background_list.append(Background(f'LevelBg{i}', (WIN_WIDTH,0)))
                return background_list
            
            case 'Player1':
                return Player('Player1', (80, TRACK_MIDDLE))
            
            case 'Opponent1':
                if game_mode != EntityFactory.current_game_mode:
                    EntityFactory.base_opponent_speed = ENTITY_SPEED['Opponent1']
                    EntityFactory.speed_increment = 0.5
                    if game_mode == MENU_OPTION[1]:
                        EntityFactory.base_opponent_speed += 1.0
                        EntityFactory.speed_increment = 0.65
                    elif game_mode == MENU_OPTION[2]:
                        EntityFactory.base_opponent_speed += 1.5
                        EntityFactory.speed_increment = 0.80
                    EntityFactory.current_game_mode = game_mode

                should_generate_opponents = (
                    current_entities is not None and
                    not any(isinstance(entity, Opponent) for entity in current_entities) and
                    not EntityFactory.new_wave_generated
                )

                if should_generate_opponents:
                    track_positions = [TRACK_TOP, TRACK_MIDDLE, TRACK_DOWN]
                    tracks = random.sample(track_positions, 2)
                    opponents = []
                    x_pos = WIN_WIDTH + 10
                    for y_pos in tracks:
                        opponent = Opponent('Opponent1', (x_pos, y_pos), speed=EntityFactory.base_opponent_speed)
                        opponents.append(opponent)
                    EntityFactory.new_wave_generated = True
                    return opponents
                
                if current_entities is not None and not any(isinstance(entity, Opponent) for entity in current_entities):
                    EntityFactory.new_wave_generated = False
                
                return []