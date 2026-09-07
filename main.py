def main():
    from logger import log_state, log_event
    import pygame
    import sys
    from constants import SCREEN_WIDTH,SCREEN_HEIGHT
    from player import Player
    from asteroid import Asteroid
    from asteroidfield import AsteroidField
    from shot import Shot

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)
    AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        for item in asteroids:
            if item.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for item in asteroids:
            for bullet in shots:
                if item.collides_with(bullet):
                    log_event("asteroid_shot")
                    item.split()
                    bullet.kill()
if __name__=="__main__":
    main()
