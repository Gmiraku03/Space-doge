from game_state import GameState
from ui import UI

from start_screen import StartScreenState
from playing import PlayingState
from game_over import GameOverState


import time

import pygame


class Game:
    # Game state
    running = True
    # Timer
    start_time = time.time()
    # UI
    ui = UI()

    def __init__(self):
        self.state = StartScreenState(self.ui)

    def handle_events(self):
        match self.state.handle_events():
            case GameState.UNCHANGED:
                pass

            case GameState.START_SCREEN:
                self.state = StartScreenState(self.ui)

            case GameState.PLAYING:
                self.start_time = time.time()
                self.state = PlayingState(self.ui)

            case GameState.GAME_OVER:
                self.state = GameOverState(self.ui, time.time() - self.start_time)

            case GameState.TERMINATED:
                self.running = False

    def update(self):
        self.state.update()

    def render(self):
        self.ui.new_frame()

        self.state.render()

        pygame.display.update()
