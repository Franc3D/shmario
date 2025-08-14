import pygame

from constants import *

def main():
    

    print("Do the shmario!")
    print(f"The screen is {SCREEN_WIDTH} by {SCREEN_HEIGHT} pixels")

    # Create a pygame GUI to be able to work on
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Managing the game time and Delta Time
    clock = pygame.time.Clock()
    deltatime = 0

    print(FIXED_FPS)

    # repeat forever and generates every frames of the game 
    while True:

        # If the player tries to quit the game using the X in the corner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Create a screen by filling it with black
        screen.fill("black")

        # This displays the current state of the screen to the window
        pygame.display.flip()

        # It makes sure to display x image every seconds
        deltatime = clock.tick(FIXED_FPS) /1000





if __name__ == "__main__":
    main()
