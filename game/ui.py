
from global_data import WIDTH, HEIGHT, WIN

import pygame


class UI:
    x = WIDTH / 2
    y = HEIGHT / 2
    spacing = 20

    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("comicsans", 30)

        pass

    def new_frame(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2

    def text(self, text):
        surf = self.font.render(text, 1, "white")
        rect = (
            surf.get_rect()
            .move(self.x, self.y)
            .move(-surf.get_width() / 2, -surf.get_height() / 2)
        )
        WIN.blit(surf, rect)

        self.y += rect.h + self.spacing

    def text_at(self, text, x, y) -> pygame.Rect:
        surf = self.font.render(text, 1, "white")
        rect = surf.get_rect().move(x, y)
        WIN.blit(surf, rect)

    def button(self, text, color) -> bool:
        surf = self.font.render(text, 1, "white")
        rect = (
            surf.get_rect()
            .move(self.x, self.y)
            .move(-surf.get_width() / 2, -surf.get_height() / 2)
        )

        self.y += rect.h + self.spacing

        pygame.draw.rect(WIN, color, rect, border_radius=5)
        WIN.blit(surf, rect)

        return rect.collidepoint(pygame.mouse.get_pos())
