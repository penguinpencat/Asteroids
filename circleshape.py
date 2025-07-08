import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.set_position(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        
    def set_position(self, x, y):
        self.position = pygame.Vector2(x, y)

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_colliding_with(self, target):
        distance_between = self.position.distance_to(target.position)
        combined_radius = self.radius + target.radius
        if distance_between > combined_radius:
            return False
        else:
            return True
        