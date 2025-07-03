import pygame

from pygame import Surface, Rect
from pygame.font import Font

from Const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Enemy import Enemy

class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('LevelBg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000
        self.entity_list.extend(EntityFactory.get_entity('Enemy1'))
        self.new_wave_generated = False


    def run(self):

        clock = pygame.time.Clock()
        running = True

        while running:

            clock.tick(60)
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    running = False

            # Se não houver inimigos e a última onda já foi gerada, prepare para nova geração
            should_generate_enemies = not any(isinstance(ent, Enemy) for ent in self.entity_list) and not self.new_wave_generated
            
            # DEBUG: Mostra posições x dos inimigos na tela
            inimigos_x = [ent.rect.x for ent in self.entity_list if isinstance(ent, Enemy)]
            print(f"[DEBUG] Inimigos na tela (x): {inimigos_x}")

            # Remove inimigos que saíram totalmente da tela à esquerda
            self.entity_list = [
                ent for ent in self.entity_list
                if not (isinstance(ent, Enemy) and ent.rect.right < 0)
            ]

            # Gera novos inimigos se necessário
            if should_generate_enemies:
                novos_inimigos = EntityFactory.get_entity('Enemy1')
                self.entity_list.extend(novos_inimigos)
                self.new_wave_generated = True

            # Reset da flag: se não houver mais nenhum inimigo
            if not any(isinstance(ent, Enemy) for ent in self.entity_list):
                self.new_wave_generated = False


            self.window.fill((0, 0, 0))    
                    
            for ent in self.entity_list:
                self.window.blit(source = ent.surf, dest = ent.rect)
                ent.move(events)

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
           
            pygame.display.flip()

        pygame.quit()
        quit()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)