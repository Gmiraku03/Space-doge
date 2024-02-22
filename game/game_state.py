from abc import ABCMeta, abstractmethod
from enum import Enum


class GameState(Enum):
    UNCHANGED = -1
    START_SCREEN = 0
    PLAYING = 1
    GAME_OVER = 2
    TERMINATED = 3


class State(metaclass=ABCMeta):
    @abstractmethod
    def current(self) -> GameState:
        pass

    @abstractmethod
    def handle_events(self) -> GameState:
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass
