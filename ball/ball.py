import sys, pygame
from ballclass import *
import ballconfig
pygame.init()

speed = [2, 2]
black = 0, 0, 0
size = ballconfig.SCREEN_WIDTH, ballconfig.SCREEN_HEIGHT

screen = pygame.display.set_mode(size)

#Managing the game's internal clock
clock = pygame.time.Clock()
deltatime = 0
fixed_fps = 60

#Create ball object taking pos (x, y) image and mass
ball = Ball(initial_speed=[1000, 300])
floor = Wall(980, 0, ballconfig.SCREEN_WIDTH, 100, color="darkgreen")
left_wall = Wall(0, 0, 100, ballconfig.SCREEN_HEIGHT, color="brown")
right_wall = Wall(0, ballconfig.SCREEN_WIDTH-100, 100, 1080, color="brown")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        
        if event.type == pygame.KEYDOWN:
            # On V keypress rotate the view type
            if event.key == pygame.K_v:
                if ballconfig.RENDERING_VISUAL and ballconfig.PHYSICS_VISUAL is False:
                    ballconfig.RENDERING_VISUAL = False
                    ballconfig.PHYSICS_VISUAL = True
                elif ballconfig.RENDERING_VISUAL is False and ballconfig.PHYSICS_VISUAL:
                    ballconfig.RENDERING_VISUAL = True
                    ballconfig.PHYSICS_VISUAL = True
                else:
                    ballconfig.RENDERING_VISUAL = True
                    ballconfig.PHYSICS_VISUAL = False
    
    # detect collisions 
    
    ball.move(deltatime)
    

    screen.fill(black)
    


    if ballconfig.PHYSICS_VISUAL:
        # Draw grid
        for x in range(0, ballconfig.SCREEN_WIDTH, 50):
            pygame.draw.line(screen, "dimgray", (x, 0), (x, 1080))
        for y in range(0, ballconfig.SCREEN_HEIGHT, 50):
            pygame.draw.line(screen, "dimgray", (0, y), (1920, y))
    
    left_wall.draw(screen)
    right_wall.draw(screen)
    floor.draw(screen)
    
    ball.draw(screen)
    pygame.display.flip()
    deltatime = clock.tick(fixed_fps) /1000

'''
Checklist
+ add downward acceleration Force = Mass*gravity
+ Do a visual for physics and a visual for rendering
    +Add a grid to the background
    +on V press switch the display mode
    -Show a line for the highest point the ball has reached per bounce
- record the max speed reached by the ball
    - Use this information to scale the squish as a % of the max speed
    - Probably need to use vector2d for the speed and orientation
- Add a data display in the top left corner with the ball's speed, position and acceleration
- add distinct mass for each ball
- squash and stretch the ball based on speed and direction
- squash the ball on impact with the walls
- add a floor and walls that the ball can bounce off of Rect.contain 
- add a controllable paddle that the ball can bounce off of
- allow player to turn off gravity
- collision by detecting if the distance between 2 balls < sum of their radius
   if they collide how to check what angle the fly towards ?

'''