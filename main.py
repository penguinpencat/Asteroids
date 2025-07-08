import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    # Creating two groups for updating and drawing
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # Creating one new group for the asteroids
    asteroids = pygame.sprite.Group()
    # Creating one new group for the bullets
    shots = pygame.sprite.Group()
    # Setting groups that the asteroid class belongs to
    Asteroid.containers = (asteroids, updatable, drawable)
    # Setting the group that the asteroid field belongs to
    AsteroidField.containers = (updatable)
    # Setting groups that the player class belongs to
    Player.containers = (updatable, drawable)
    # Setting groups that the shot class belongs to
    Shot.containers = (shots, updatable, drawable)
    # Creating the player
    player = Player(x, y)
    # Creating the asteroid
    asteroidfield = AsteroidField()
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        # Fill the screen with (insert_fav_colour)
        screen.fill((20, 41, 67))
        # Fill the screen with black
        # Screen.fill((0, 0, 0))
        # Updating players position
        updatable.update(dt)
        # Iterating over all objects in asteroids
        for asteroid in asteroids:
            if asteroid.is_colliding_with(player) == True:
                print("Game over!")
                sys.exit()
        # Re-drawing the player
        for drawing in drawable:
            drawing.draw(screen)
        # Update the display
        pygame.display.flip()
        miliseconds = clock.tick(60)
        dt = miliseconds / 1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
