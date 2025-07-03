from code.Entity import Entity
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory

class EntityMediator:
    
    @staticmethod
    def __verify_collision_window(ent: Entity) -> bool:
        if isinstance(ent, Enemy):
            # Retorna False se o inimigo saiu totalmente da tela à esquerda
            return ent.rect.right >= 0
        return True

    @staticmethod
    def verify_collision(entity_list: list[Entity]) -> list[Entity]:
        # Filtra entidades, mantendo apenas aquelas que passam na verificação
        filtered_list = [ent for ent in entity_list if EntityMediator.__verify_collision_window(ent)]
        
        # Adiciona novos inimigos se necessário
        novos_inimigos = EntityFactory.get_entity('Enemy1', current_entities=filtered_list)
        if novos_inimigos:
            filtered_list.extend(novos_inimigos)
        
        return filtered_list