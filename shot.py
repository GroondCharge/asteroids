from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, position: pygame.Vector2, velocity: pygame.Vector2):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        #self.position = position
        self.velocity = velocity
    def update(self, dt):
        self.position += self.velocity * dt
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 1)

        
