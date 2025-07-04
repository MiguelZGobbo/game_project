from code.Entity import Entity
from code.Opponent import Opponent
from code.Player import Player
from code.EntityFactory import EntityFactory

class EntityMediator:
    collision_detected = False

    @staticmethod
    def verify_collision_window(entity: Entity) -> bool:
        if isinstance(entity, Opponent):
            return entity.rect.right >= 0
        return True

    @staticmethod
    def verify_player_opponent_collision(player: Entity, opponents: list[Entity]) -> bool:
        collision_occurring = False
        for opponent in opponents:
            if isinstance(opponent, Opponent):
                right_of_left = player.rect.right >= opponent.rect.left
                left_of_right = player.rect.left <= opponent.rect.right
                bottom_below_top = player.rect.bottom >= opponent.rect.top
                top_above_bottom = player.rect.top <= opponent.rect.bottom

                if right_of_left and left_of_right and bottom_below_top and top_above_bottom:
                    collision_occurring = True
                    EntityMediator.collision_detected = True
                    break

        if not collision_occurring and EntityMediator.collision_detected:
            EntityMediator.collision_detected = False

        return collision_occurring

    @staticmethod
    def verify_collision(entity_list: list[Entity], game_mode: str) -> list[Entity]:
        initial_opponent_count = sum(1 for entity in entity_list if isinstance(entity, Opponent))
        
        filtered_list = [entity for entity in entity_list if EntityMediator.verify_collision_window(entity)]
        
        final_opponent_count = sum(1 for entity in filtered_list if isinstance(entity, Opponent))
        
        if initial_opponent_count > final_opponent_count:
            EntityFactory.base_opponent_speed += EntityFactory.speed_increment

        player = next((entity for entity in filtered_list if isinstance(entity, Player)), None)
        
        if player:
            EntityMediator.verify_player_opponent_collision(player, filtered_list)
        
        new_opponents = EntityFactory.get_entity('Opponent1', current_entities=filtered_list, game_mode=game_mode)
        if new_opponents:
            filtered_list.extend(new_opponents)
        
        return filtered_list