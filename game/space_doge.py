from game import Game

import pygame


def main():
    game = Game()

    while game.running:
        game.handle_events()
        game.update()
        game.render()

    pygame.quit()


if __name__ == "__main__":
    main()
