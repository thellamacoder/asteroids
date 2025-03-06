import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    #print(f"Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    # Initialize Pygame
    pygame.init()
    # Define the game's screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create a clock object to limit the refresh rate for the screen
    clock = pygame.time.Clock()
    # Delta time (dt) to hold the change in time
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        pygame.Surface.fill(screen,color="black", )

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # this is the end of the game loop
        # the game loop won't exceed the tick time (in this case, the loop will 
        # wait until 1/60th of a second has passed)
        clock.tick(60)
        dt = (clock.get_time()/1000)

# This is the end of the file

if __name__ == "__main__":
    main()