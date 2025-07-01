import pygame

from Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from Level import Level

class Game:
    
    def  __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level inicial', menu_return )
                level_return = Level.run()

            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                quit()
            
            else:
                pass

