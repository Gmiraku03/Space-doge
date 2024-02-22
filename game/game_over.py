from game_state import GameState, State
from ui import UI

import pygame

class GameOverState(State):
    def __init__(self, ui: UI, score):
        self.ui = ui
        self.should_restart = False
        self.should_quit = False

        self.score = round(score)

    def current(self) -> GameState:
        return GameState.GAME_OVER

    def handle_events(self) -> GameState:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState.TERMINATED
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.should_restart:
                    return GameState.PLAYING
                elif self.should_quit:
                    return GameState.TERMINATED

        return GameState.UNCHANGED

    def update(self):
        pass

    def render(self):
        self.ui.text(f"You lost! Score {self.score}")

        self.should_restart = self.ui.button("Restart", "green")
        self.should_quit = self.ui.button("Quit", "red")
