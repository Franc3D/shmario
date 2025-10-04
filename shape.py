import pygame

class circleshape: #to be overwritten
    def __init__(self, x, y, radius):
        
        # something about groups to use later... not sure what
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()


        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, deltatime):
        pass    


