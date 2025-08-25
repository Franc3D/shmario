import pygame

class circleshape: #to be overwritten
    def __init__(self, x, y, radius):
        
        
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()


        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (self.x, self.y), self.radius)

    def update(self, deltatime):
        pass    