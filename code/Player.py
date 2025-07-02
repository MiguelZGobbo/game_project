import pygame

from Const import TRACK_TOP, TRACK_MIDDLE, TRACK_DOWN 
from code.Entity import Entity

class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.current_track = 1

    def update(self):
        pass

    def move(self, events):
        
        for event in events:
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.current_track > 0:
                            self.current_track -= 1
                    elif event.key == pygame.K_DOWN:
                        if self.current_track < 2:
                            self.current_track += 1

                    if self.current_track == 0:
                        self.rect.centery = TRACK_TOP
                    elif self.current_track == 1:
                        self.rect.centery = TRACK_MIDDLE
                    elif self.current_track == 2:
                        self.rect.centery = TRACK_DOWN

                