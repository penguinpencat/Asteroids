import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TEXT_COLOUR

def show_game_over(screen):
    font = pygame.font.SysFont(None, 72)
    text = font.render("Game Over!", True, TEXT_COLOUR)
    rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, rect)
    pygame.display.flip()
    # Wait for the user to close the window or press a key
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                waiting = False