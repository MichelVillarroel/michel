import pygame
from game.components.power_ups.power_up import PowerUp
from game.utils.constants import HEART, HEART_TYPE


class Heart(PowerUp):
    def __init__(self):
        super().__init__(HEART, HEART_TYPE)
        self.lives = 1

    def update(self, game_speed, power_ups):
        super().update(game_speed, power_ups)

    def draw(self, screen):
        super().draw(screen)

