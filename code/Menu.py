import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Const import COLOR_WHITE, WIN_WIDTH, MENU_OPTION


class Menu:
    
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Menubackground.png')
        self.rect = self.surf.get_rect(left = 0, top = 0)

    def run(self):

        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source = self.surf, dest = self.rect)
            
            for i in range(len(MENU_OPTION)):
                
                self.menu_text(60, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH/2), 335 + 50 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name = 'Lucida Sans Typewriter', size = text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(source = text_surf, dest = text_rect)


        
