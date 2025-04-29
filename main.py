import pygame
from constants import *
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    Fpsclock = pygame.time.Clock()
    dt = 0
    The_player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

# Game Loop
    infinite = 0
    while infinite == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = Fpsclock.tick(60) / 1000
        
        
        pygame.Surface.fill(screen, ("black"))
        The_player.draw(screen)
        pygame.display.flip()












if __name__ == "__main__":
    main()   