import time
import random

from game_state import GameState, State
from global_data import WIDTH, HEIGHT, WIN, BG
from ui import UI

import pygame

PLAYER_RADIUS = 20
PLAYER_VEL = 5

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3


class PlayingState(State):
    # Game state
    hit = False
    wait_for_draw = False
    lives = 3

    # Timer
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    def __init__(self, ui: UI):
        self.ui = ui
        self.player = pygame.Rect(
            WIDTH / 2 - PLAYER_RADIUS,
            HEIGHT - 2 * PLAYER_RADIUS - 20,
            2 * PLAYER_RADIUS,
            2 * PLAYER_RADIUS,
        )
        self.stars = []
        self.star_count = 0
        self.star_add_increment = 2000
        self.start_time = time.time()
        self.elapsed_time = 0

    def current(self) -> GameState:
        return GameState.PLAYING

    def handle_events(self) -> GameState:
        if self.hit:
            self.lives -= 1
            self.reset()

            if self.lives == 0:
                return GameState.GAME_OVER

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState.TERMINATED

        return GameState.UNCHANGED

    def update(self):
        self.star_count += self.clock.tick(60)
        self.elapsed_time = time.time() - self.start_time

        if self.star_count > self.star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                self.stars.append(star)
            self.star_add_increment = max(200, self.star_add_increment - 50)
            self.star_count = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.player.x - PLAYER_VEL >= 0:
            self.player.x -= PLAYER_VEL
        if (
            keys[pygame.K_RIGHT]
            and self.player.x + PLAYER_VEL + self.player.width <= WIDTH
        ):
            self.player.x += PLAYER_VEL

        for star in self.stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                self.stars.remove(star)
            elif star.y + star.height >= self.player.y and star.colliderect(
                self.player
            ):
                self.hit = True
                return

    def render(self):
        WIN.blit(BG, (0, 0))

        self.ui.text_at(f"Time: {round(self.elapsed_time)}s", 10, 10)
        self.ui.text_at(f"Lives: {self.lives}", 10, 50)

        pygame.draw.circle(
            WIN,
            "red",
            (self.player.x + PLAYER_RADIUS, self.player.y + PLAYER_RADIUS),
            20,
        )
        # pygame.draw.rect(WIN, "red", self.player)
        for star in self.stars:
            pygame.draw.rect(WIN, "white", star)

        if self.wait_for_draw:
            self.wait_for_draw = False
            pygame.display.update()
            pygame.time.delay(2000)

    def reset(self):
        self.player = pygame.Rect(
            WIDTH / 2 - PLAYER_RADIUS,
            HEIGHT - 2 * PLAYER_RADIUS - 20,
            2 * PLAYER_RADIUS,
            2 * PLAYER_RADIUS,
        )

        self.stars = []
        self.star_count = 0
        self.star_add_increment = 2000
        self.start_time = time.time()

        self.hit = False
        self.wait_for_draw = True
