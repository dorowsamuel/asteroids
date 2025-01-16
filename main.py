import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update and draw game objects
        screen.fill((0, 0, 0))
        player.update(dt)
        player.draw(screen)

        # render updated game state and tick game clock
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()