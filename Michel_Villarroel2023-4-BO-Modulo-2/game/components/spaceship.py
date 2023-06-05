import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TYPE
from game.components.bullets.bullet import Bullet

class Spaceship(Sprite):

    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.direction = 1  #almacenar direccion
        self.type = "player"
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0
        self.lives = 0  # Añadir atributo para almacenar las vidas del jugador

    def update(self, user_input, game):
      if user_input[pygame.K_LEFT]:
        self.move_left()
      elif user_input[pygame.K_RIGHT]:
        self.move_rigth()
      elif user_input[pygame.K_UP]:
        self.move_up()
      elif user_input[pygame.K_DOWN]:
        self.move_down()
      elif user_input[pygame.K_a]:
        self.shoot(game)

    def move_left(self):
        if self.rect.left > 0:
          self.rect.x -= self.SHIP_SPEED
        else:                      #cambia la direcion
          self.rect.x = SCREEN_WIDTH - self.SHIP_WIDTH
          self.direction = -1

    def move_rigth(self):
        if self.rect.right < SCREEN_WIDTH:
          self.rect.x += self.SHIP_SPEED
        else:                       #mueve la direcion a la derecha
          self.rect.x = 0
          self.direction = 1 

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPEED

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += self.SHIP_SPEED

    def draw(self, screen):
      if self.direction == 1:
          screen.blit(self.image, (self.rect.x, self.rect.y))
      else:                            #voltea la imagen antes draw
        flipped_image = pygame.transform.flip(self.image, True, False)
        screen.blit(flipped_image, (self.rect.x, self.rect.y))

    def shoot(self, game):
      bullet = Bullet(self)
      game.bullet_manager.add_bullet(bullet)

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS


    def set_image(self, size = (SHIP_WIDTH, SHIP_HEIGHT), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

    def add_lives(self, num_lives):
        self.lives += num_lives

    def get_lives(self):
        return self.lives
