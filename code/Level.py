import pygame

from pygame import Surface, Rect
from pygame.font import Font

from Const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator

class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('LevelBg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(60)
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    running = False

            # Atualiza a lista de entidades com verificação, remoção e adição feita pelo EntityMediator
            self.entity_list = EntityMediator.verify_collision(entity_list=self.entity_list)

            # Renderiza as entidades na tela
            self.window.fill((0, 0, 0))    
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move(events)

            # Exibe textos na tela
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