import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_WHITE, WIN_WIDTH, MENU_OPTION, COLOR_BLACK

class Menu:
    def __init__(self, window):
        self.window = window
        self.surface = pygame.image.load('./asset/Menubackground.png').convert_alpha()
        self.rect = self.surface.get_rect(left=0, top=0)

    def run(self):
        selected_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surface, dest=self.rect)
            
            for i in range(len(MENU_OPTION)):
                if i == selected_option:
                    self.menu_text(60, MENU_OPTION[i], COLOR_BLACK, (WIN_WIDTH/2, 335 + 50 * i))
                else:
                    self.menu_text(60, MENU_OPTION[i], COLOR_WHITE, (WIN_WIDTH/2, 335 + 50 * i))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if selected_option < len(MENU_OPTION) - 1:
                            selected_option += 1
                        else:
                            selected_option = 0
                    if event.key == pygame.K_UP:
                        if selected_option > 0:
                            selected_option -= 1
                        else:                         
                            selected_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[selected_option]
            
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(source=text_surface, dest=text_rect)