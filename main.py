import pygame

from constants import *
from shape import *
from entity import *

def main():
    

    print("Do the shmario!")
    print(f"The screen is {SCREEN_WIDTH} by {SCREEN_HEIGHT} pixels")

    # Create a pygame GUI to be able to work on
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #user_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 50)

    # Managing the game time and Delta Time
    clock = pygame.time.Clock()
    deltatime = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    grounded = False
    y_momentum = 0.0

    print(FIXED_FPS)

    # repeat forever and generates every frames of the game 
    while True:

        # If the player tries to quit the game using the X in the corner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Create a screen by filling it with black, erasing the previous frame
        screen.fill("black")


        # make level here
        pygame.draw.rect(screen, "green", pygame.Rect(0, screen.get_height() - 100,screen.get_width(), 100))

        
        pygame.draw.circle(screen, "red", player_pos, 10)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if grounded == True:
                y_momentum = -1000
                grounded = False
        if keys[pygame.K_a]:
            player_pos.x -= 300 * deltatime
        if keys[pygame.K_d]:
            player_pos.x += 300 * deltatime

        if grounded == False:
            player_pos.y += y_momentum * deltatime
            y_momentum += 50
            if player_pos.y >= screen.get_height() - 100 - 10:
                player_pos.y = screen.get_height() - 100 - 10
                grounded = True
                y_momentum = 0.0


        # This displays the current state of the screen to the window
        pygame.display.flip()

        # It makes sure to display x image every seconds
        deltatime = clock.tick(FIXED_FPS) /1000 
        # .tick() calculates the time since the last call to .tick()
        # adding a value to .tick() will cap the framerate to that value
        





if __name__ == "__main__":
    main()
