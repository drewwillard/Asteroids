import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    #startup messages
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    #initialize display and clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    #create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    #assign objects to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (all_asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    #init player field
    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    main_field = AsteroidField()
    
    # Main game loop
    while True:
        game_clock.tick(FPS)
        dt = game_clock.get_time() / 1000

        for event in pygame.event.get(): #exit if window closed
            if event.type == pygame.QUIT:
                return
        for item in updatable:
            item.update(dt)
        pygame.Surface.fill(screen, (0, 0, 0)) #black screen
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()