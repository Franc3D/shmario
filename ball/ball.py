import sys, pygame
from ballclass import *
pygame.init()

size = width, height = 1500, 1400
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

#Managing the game's internal clock
clock = pygame.time.Clock()
deltatime = 0
fixed_fps = 60

#Create ball object taking pos (x, y) image and mass
ball = Ball(initial_speed=[300, 300])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    
    # detect collisions 
    
    ball.move(deltatime)
    

    screen.fill(black)
    ball.draw(screen)
    pygame.display.flip()
    deltatime = clock.tick(fixed_fps) /1000

'''
Checklist
- add downward acceleration Force = Mass*gravity
- add a floor and walls that the ball can bounce off of
- add a controllable paddle that the ball can bounce off of
- allow player to turn off gravity
'''