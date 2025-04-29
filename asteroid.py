from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        new_angle = random.uniform(20,50)
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_velocity1 = self.velocity.rotate(new_angle)
            new_velocity2 = self.velocity.rotate(new_angle * -1)
            new_rock1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_rock2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_rock1.velocity = (new_velocity1 * 1.2)
            new_rock2.velocity = (new_velocity2 * 1.2)
            