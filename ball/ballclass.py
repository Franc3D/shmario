from pygame import *
import ballconfig
from math import sqrt

_gravity = 9.81 * 100  # pixels per second squared
_air_resistance = 0.00001 *8

class Ball:
    def __init__(self, image_path="intro_ball.gif", position = (100, 100), mass = 1, size_pixel = None, initial_speed = [0, 0], squish_percent = 50):
        self.image = image.load(image_path)
        if size_pixel != None:      
            self.image = transform.scale(self.image, (size_pixel, size_pixel))
            self.size = size_pixel
        else:
            self.size = self.image.get_width()

        self.mass = mass
        self.speed = list(initial_speed)
        self.position = list(position)
        self.squish = squish_percent




    def move(self, deltatime):
        
        # normalize speed vector
        v = sqrt(self.speed[0]**2 + self.speed[1]**2)
        n = [
            self.speed[0] / v if v != 0 else 0.0001,
            self.speed[1] / v if v != 0 else 0.0001
        ]

        self.position =  [
            self.position[0] + self.speed[0] * deltatime,
            self.position[1] + self.speed[1] * deltatime
        ]
        self.speed = [
            self.speed[0] -_air_resistance * n[0] * v*v * deltatime,
            self.speed[1] + (_gravity * deltatime) - _air_resistance * n[1] * v*v * deltatime
        ]
        
        
        # detect collision with walls
        if self.position[0] - (self.size / 2) < 0 or self.position[0] + (self.size / 2) > 1920:
            self.speed[0] = -self.speed[0]
        if self.position[1] - (self.size / 2) < 0 or self.position[1] + (self.size / 2) > 1080:
            self.speed[1] = -self.speed[1]

        #print(self.position)
        
    
    def detect_collision(self, rect):
        #TO DO TOMORROW
        pass

    def draw(self, surface):
        if ballconfig.RENDERING_VISUAL:
            self.rectangle = self.image.get_rect(center = self.position)
            surface.blit(self.image, self.rectangle)

        if ballconfig.PHYSICS_VISUAL:
            # Draw squish max range
            draw.circle(surface, "yellow", self.position, self.size/2 * (self.squish/100), 2)
            draw.circle(surface, "cyan", self.position, self.size/2, 2)

class Wall:
    def __init__(self, top, left, width, height, color="white"):
        
        self.rectangle = Rect(left, top, width, height)
        self.top = top 
        self.left = left
        self.width = width
        self.height = height
        self.color = color
    
    def get_collision(self):
        return self.rectangle
    
    def draw(self, surface):
        if ballconfig.RENDERING_VISUAL:
            draw.rect(surface, self.color, self.rectangle)
        if ballconfig.PHYSICS_VISUAL:
            draw.rect(surface, "red", self.rectangle, 2)
        
