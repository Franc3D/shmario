import sys, pygame
from ballclass import *
pygame.init()

size = width, height = 1920, 1080
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

#Managing the game's internal clock
clock = pygame.time.Clock()
deltatime = 0
fixed_fps = 60

#Create ball object taking pos (x, y) image and mass
ball = Ball(initial_speed=[1000, 300])
floor = Wall(980, 0, 1920, 100, color="green")
left_wall = Wall(0, 0, 100, 1080, color="brown")
right_wall = Wall(0, 1820, 100, 1080, color="brown")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    
    # detect collisions 
    
    ball.move(deltatime)
    

    screen.fill(black)
    
    left_wall.draw(screen)
    right_wall.draw(screen)
    floor.draw(screen)
    
    ball.draw(screen)
    pygame.display.flip()
    deltatime = clock.tick(fixed_fps) /1000

'''
Checklist
+ add downward acceleration Force = Mass*gravity
- add distinct mass for each ball
- squash and stretch the ball based on speed and direction
- squash the ball on impact with the walls
- add a floor and walls that the ball can bounce off of
- add a controllable paddle that the ball can bounce off of
- allow player to turn off gravity
- collision by detecting if the distance between 2 balls < sum of their radius
   if they collide how to check what angle the fly towards ?

'''