from Entity import Entity

class Background(Entity):
    
    def __innit__(self, name: str, position: tuple):
        super().__init__(name, position)
        

    def move(self):
        pass