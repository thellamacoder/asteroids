import pygame
from constants import *
from circleshape import CircleShape
from player import Player

def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    # Initialize Pygame
    pygame.init()
    # Define the game's screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Create a clock object to limit the refresh rate for the screen
    clock = pygame.time.Clock()
    # Delta time (dt) to hold the change in time
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,color="black", )
        player.draw(screen)
        pygame.display.flip()
        

        # this is the end of the game loop
        # the game loop won't exceed the tick time (in this case, the loop will 
        # wait until 1/60th of a second has passed)
        clock.tick(60)
        dt = (clock.get_time()/1000)

# This is the end of the file

if __name__ == "__main__":
    main()