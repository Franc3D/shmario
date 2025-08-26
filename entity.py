

class Entity():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.direction = "right"
        self.is_grounded = False
        self.is_jumping = False
        
        self.sprite = None
        self.animation_state = "idle"
        
        #self.hitbox = 
        self.color = (255, 255, 255)  # Default color is white
        