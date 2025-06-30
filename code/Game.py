import pygame

class Game:
    def  __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(300, 200))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()