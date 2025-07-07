from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen, 
            color=(255, 255, 255), 
            center=self.position,
            radius=self.radius,
            width=2
        )
    
    def update(self, dt):
        # Moving forward
        self.position += self.velocity * dt
