import pygame
from constants import *
from player import Player

def main():
    # Initialize Pygame
    pygame.init()
    #Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()
    dt = 0
    # Player starting position
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        # Fill the screen with (insert_fav_colour)
        screen.fill((20, 41, 67))
        # Fill the screen with black
        #screen.fill((0, 0, 0))
        # Updating players position
        player.update(dt)
        # Re-drawing the player
        player.draw(screen)
        # Update the display
        pygame.display.flip()
        miliseconds = clock.tick(60)
        dt = miliseconds / 1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
