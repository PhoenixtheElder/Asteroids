import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Groups!
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    
    
    
    
    Fpsclock = pygame.time.Clock()
    dt = 0
    The_player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    The_Asteroid = AsteroidField()

# Game Loop
    infinite = 0
    while infinite == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = Fpsclock.tick(60) / 1000
        
        
        pygame.Surface.fill(screen, ("black"))
        updatable.update(dt)
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()

        for entity in asteroids:
            if entity.collision(The_player) == True:
                print("Game Over")
                return
        for bullet in shots:
            for rock in asteroids:
                if rock.collision(bullet) == True:
                    if rock.alive() and bullet.alive():
                        rock.split()
                        bullet.kill()
                        break











if __name__ == "__main__":
    main()   