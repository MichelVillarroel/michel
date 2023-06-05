import random
import pygame
from game.components.power_ups.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD
from game.components.power_ups.heart import Heart



class PowerUpManager():
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(4000, 8000)
        self.reset_time_power = self.when_appears
        self.duration = random.randint(3, 5)
        self.player_lives = 0  # Añadir atributo para almacenar las vidas del jugador

    def generate_power_up(self, game):
        power_up_classes = [Shield, Heart]
        power_up_class = random.choice(power_up_classes)
        power_up = power_up_class()
        if isinstance(power_up, Heart):
            game.player.add_lives(power_up.lives)
        #    game.player.lives += power_up.lives
        self.reset_time_power
        self.power_ups.append(power_up)
        self.when_appears += random.randint(3000, 7000)
        self.power_ups.append(power_up)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up(game)# Pasar el argumento 'game' al llamar a la función

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                power_up.star_time = pygame.time.get_ticks()
                if isinstance(power_up, Heart):
                    game.player.add_lives(power_up.lives)# Aumentar las vidas del jugador
                    self.player_lives = game.player.get_lives()# Actualizar el contador de vidas

                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_time_up = power_up.star_time + (self.duration * 1000)
                game.player.set_image((65, 75), SPACESHIP_SHIELD)
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(now + 5000, now + 10000)