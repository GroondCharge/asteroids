# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	AsteroidField.containers = (updatable)
	asteroidfield = AsteroidField()
	Asteroid.containers = (asteroids, updatable, drawable)
	Player.containers = (updatable, drawable)
	Shot.containers = (drawable, updatable, shots)
	print("Starting asteroids!")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		screen.fill("black")
		for member in updatable:
			#player.draw(screen)
			member.update(dt)
		for member in asteroids:
			if member.collision(player):
				print("Game over")
				sys.exit()
		for member in drawable:
			member.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60)
		dt /= 1000
if __name__ == "__main__":
    main()
