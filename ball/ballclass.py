from pygame import *
from math import sqrt

_gravity = 9.81 * 100  # pixels per second squared
_air_resistance = 0.00001 *5

class Ball:
    def __init__(self, image_path="intro_ball.gif", position = (100, 100), mass = 1, size_pixel = 50, initial_speed = [0, 0]):
        self.image = image.load(image_path)      
        self.image = transform.scale(self.image, (size_pixel, size_pixel))

        self.mass = mass
        self.speed = list(initial_speed)
        self.position = list(position)




    def move(self, deltatime):

        # normalize speed vector
        v = sqrt(self.speed[0]**2 + self.speed[1]**2)
        n = [
            self.speed[0] / v if v != 0 else 1,
            self.speed[1] / v if v != 0 else 1
        ]

        self.position =  [
            self.position[0] + self.speed[0] * deltatime,
            self.position[1] + self.speed[1] * deltatime
        ]
        self.speed = [
            self.speed[0] -_air_resistance * n[0] * v*v * deltatime,
            self.speed[1] + (_gravity * deltatime) - _air_resistance * n[1] * v*v * deltatime
        ]
        
        

        if self.position[0] < 0 or self.position[0] > 1500:
            self.speed[0] = -self.speed[0]
        if self.position[1] < 0 or self.position[1] > 1400:
            self.speed[1] = -self.speed[1]
        

    def draw(self, surface):
        self.rectangle = self.image.get_rect(center = self.position)
        surface.blit(self.image, self.rectangle)
