import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    all_shots = pygame.sprite.Group()
    #assign objects to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (all_asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (all_shots, updatable, drawable)

    #init player field
    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    main_field = AsteroidField()
    
    # GAME LOOP
    while True:
        game_clock.tick(FPS)
        dt = game_clock.get_time() / 1000

        for event in pygame.event.get(): #exit if window closed
            if event.type == pygame.QUIT:
                return
        for item in updatable:
            item.update(dt)
        for asteroid in all_asteroids:
            if player_1.collision_check(asteroid) == True:
                print("Game over!")
                SystemExit()
                return
            for shot in all_shots:
                if shot.collision_check(asteroid) == True:
                    asteroid.split()
        pygame.Surface.fill(screen, (0, 0, 0)) #black screen
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()