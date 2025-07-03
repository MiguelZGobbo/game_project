import pygame
from pygame import Surface, Rect
from pygame.font import Font

from Const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.Entity import Entity
from code.Player import Player
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Menu import Menu

class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('LevelBg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000
        self.score = 0
        self.last_score_time = pygame.time.get_ticks()  # Tempo do último reset ou início

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(60)
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Passa o game_mode para a verificação de colisão
            self.entity_list = EntityMediator.verify_collision(entity_list=self.entity_list, game_mode=self.game_mode)

            # Verifica colisão para pontuação
            player = next((ent for ent in self.entity_list if isinstance(ent, Player)), None)
            if player:
                collision_occurring = EntityMediator._EntityMediator__verify_player_enemy_collision(player, self.entity_list)
                if collision_occurring:
                    # Volta ao menu após colisão
                    return  # Retorna ao menu principal no Game.py

            # Atualiza pontuação se não houver colisão (1 ponto a cada 30 segundos)
            current_time = pygame.time.get_ticks()
            time_elapsed = (current_time - self.last_score_time) // 250  # Segundos completos
            if time_elapsed > 0:
                self.score += time_elapsed  # Incrementa 1 ponto a cada 30 segundos
                self.last_score_time = current_time

            # Renderiza as entidades na tela
            self.window.fill((0, 0, 0))    
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move(events)

            # Exibe textos na tela
            # Pontuação (esquerda)
            self.level_text(22, f'Pontuação: {self.score}', COLOR_WHITE, (10, 5))
            # FPS (canto superior direito)
            self.level_text(22, f'FPS: {clock.get_fps():.0f}', COLOR_WHITE, (WIN_WIDTH - 10, 5), align_right=True)

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, align_right: bool = False):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect()
        
        # Define a posição do texto
        if align_right:
            text_rect.right = text_pos[0]
            text_rect.top = text_pos[1]
        else:
            text_rect.left = text_pos[0]
            text_rect.top = text_pos[1]
        
        self.window.blit(source=text_surf, dest=text_rect)