import pygame
from constants import *


def main():
    # Initialize Pygame
    pygame.init()
    #Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()
    dt = 0
    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        # Fill the screen with black
        screen.fill((0, 0, 0))
        # Update the display
        pygame.display.flip()
        miliseconds = clock.tick(60)
        dt = miliseconds / 1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()