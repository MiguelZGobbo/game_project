from code.Entity import Entity
from code.Enemy import Enemy
from code.Player import Player
from code.EntityFactory import EntityFactory

class EntityMediator:
    _collision_detected = False  # Flag para rastrear colisão ativa

    @staticmethod
    def __verify_collision_window(ent: Entity) -> bool:
        if isinstance(ent, Enemy):
            # Retorna False se o inimigo saiu totalmente da tela à esquerda
            return ent.rect.right >= 0
        return True

    @staticmethod
    def __verify_player_enemy_collision(player: Entity, enemies: list[Entity]) -> bool:
        """Verifica se o jogador colidiu com algum inimigo usando lógica personalizada."""
        collision_occurring = False
        for enemy in enemies:
            if isinstance(enemy, Enemy):
                # Verifica as quatro condições de colisão
                right_of_left = player.rect.right >= enemy.rect.left
                left_of_right = player.rect.left <= enemy.rect.right
                bottom_below_top = player.rect.bottom >= enemy.rect.top
                top_above_bottom = player.rect.top <= enemy.rect.bottom

                # Se todas as condições forem verdadeiras, há colisão
                if right_of_left and left_of_right and bottom_below_top and top_above_bottom:
                    collision_occurring = True
                    if not EntityMediator._collision_detected:
                        print("Colisão detectada entre Player1 e Enemy!")
                        EntityMediator._collision_detected = True
                    break  # Sai do loop após detectar a primeira colisão

        # Reseta a flag se não houver mais colisão
        if not collision_occurring and EntityMediator._collision_detected:
            EntityMediator._collision_detected = False

        return collision_occurring

    @staticmethod
    def verify_collision(entity_list: list[Entity]) -> list[Entity]:
        # Filtra entidades, mantendo apenas aquelas que passam na verificação
        filtered_list = [ent for ent in entity_list if EntityMediator.__verify_collision_window(ent)]
        
        # Encontra o jogador na lista
        player = next((ent for ent in filtered_list if isinstance(ent, Player)), None)
        
        # Verifica colisão entre jogador e inimigos, se o jogador existir
        if player:
            EntityMediator.__verify_player_enemy_collision(player, filtered_list)
        
        # Adiciona novos inimigos se necessário
        novos_inimigos = EntityFactory.get_entity('Enemy1', current_entities=filtered_list)
        if novos_inimigos:
            filtered_list.extend(novos_inimigos)
        
        return filtered_list