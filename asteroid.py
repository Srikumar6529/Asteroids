from circleshape import CircleShape
import pygame,random
from constants import *
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self,x: float, y: float, radius: float) -> None:
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        kid1 = self.velocity.rotate(angle)
        kid2 = self.velocity.rotate(-angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        as1 = Asteroid(self.position[0],self.position[1],new_rad)
        as1.velocity = kid1 * 1.2
        as2 = Asteroid(self.position[0],self.position[1],new_rad)
        as2.velocity = kid2 *1.2

