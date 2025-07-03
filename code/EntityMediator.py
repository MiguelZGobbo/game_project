from code.Entity import Entity
from code.Enemy import Enemy
from code.Player import Player
from code.EntityFactory import EntityFactory

class EntityMediator:
    _collision_detected = False

    @staticmethod
    def __verify_collision_window(ent: Entity) -> bool:
        if isinstance(ent, Enemy):
            return ent.rect.right >= 0
        return True

    @staticmethod
    def __verify_player_enemy_collision(player: Entity, enemies: list[Entity]) -> bool:
        collision_occurring = False
        for enemy in enemies:
            if isinstance(enemy, Enemy):
                right_of_left = player.rect.right >= enemy.rect.left
                left_of_right = player.rect.left <= enemy.rect.right
                bottom_below_top = player.rect.bottom >= enemy.rect.top
                top_above_bottom = player.rect.top <= enemy.rect.bottom

                if right_of_left and left_of_right and bottom_below_top and top_above_bottom:
                    collision_occurring = True
                    if not EntityMediator._collision_detected:
                        print("Colisão detectada entre Player1 e Enemy!")
                        EntityMediator._collision_detected = True
                    break

        if not collision_occurring and EntityMediator._collision_detected:
            EntityMediator._collision_detected = False

        return collision_occurring

    @staticmethod
    def verify_collision(entity_list: list[Entity], game_mode: str) -> list[Entity]:
        initial_enemy_count = sum(1 for ent in entity_list if isinstance(ent, Enemy))
        
        filtered_list = [ent for ent in entity_list if EntityMediator.__verify_collision_window(ent)]
        
        final_enemy_count = sum(1 for ent in filtered_list if isinstance(ent, Enemy))
        
        # Incrementa a velocidade base se inimigos foram excluídos
        if initial_enemy_count > final_enemy_count:
            EntityFactory._base_enemy_speed += EntityFactory._speed_increment
            print(f"[EntityMediator] Inimigos excluídos - Velocidade atual: {EntityFactory._base_enemy_speed}")

        player = next((ent for ent in filtered_list if isinstance(ent, Player)), None)
        
        if player:
            EntityMediator.__verify_player_enemy_collision(player, filtered_list)
        
        # Adiciona novos inimigos, passando o game_mode
        novos_inimigos = EntityFactory.get_entity('Enemy1', current_entities=filtered_list, game_mode=game_mode)
        if novos_inimigos:
            filtered_list.extend(novos_inimigos)
        
        return filtered_list