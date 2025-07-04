from abc import ABC, abstractmethod
import pygame

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surface = pygame.image.load(f'./asset/{name}.png').convert_alpha()
        self.rect = self.surface.get_rect(left=position[0], top=position[1])
        self.speed = 0
    
    @abstractmethod
    def move(self):
        pass