from game_state import GameState, State
from global_data import BG, WIN
from ui import UI

import pygame


class StartScreenState(State):
    def __init__(self, ui: UI):
        self.ui = ui

    def current(self) -> GameState:
        return GameState.START_SCREEN

    def handle_events(self) -> GameState:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState.TERMINATED
            elif event.type == pygame.KEYDOWN:
                return GameState.PLAYING

        return GameState.UNCHANGED

    def update(self):
        pass

    def render(self):
        WIN.blit(BG, (0, 0))

        self.ui.text("Space Doge")
        self.ui.text("Press any key to start")
