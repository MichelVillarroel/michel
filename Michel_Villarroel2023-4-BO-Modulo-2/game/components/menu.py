import pygame

from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Menu:  
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH //2 

    def __init__(self, message, screen):
      screen.fill((255, 255, 255))
      self.font = pygame.font.Font(FONT_STYLE, 30)
      self.text = self.font.render(message, True, (0, 0, 0))
      self.text_rect = self.text.get_rect()
      self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

      self.text0 = self.font.render(message, True, (0, 0, 0))
      self.text_rect0 = self.text0.get_rect()
      self.text_rect0.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

      self.text1 = self.font.render(message, True, (0, 0, 0))
      self.text_rect1 = self.text1.get_rect()
      self.text_rect1.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

      self.text2 = self.font.render(message, True, (0, 0, 0))
      self.text_rect2 = self.text2.get_rect()
      self.text_rect2.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

    def update(self, game):
       pygame.display.update()
       self.handle_events_on_menu(game)

    def draw(self, screen):
       screen.blit(self.text, self.text_rect)
       screen.blit(self.text0, self.text_rect0)
       screen.blit(self.text1, self.text_rect1)
       screen.blit(self.text2, self.text_rect2)

    def draw_shield(self, screen, message, x = 550, y = 50, color = (255, 255, 255)):
        text = self.font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)

    def handle_events_on_menu(self, game):
       for event in pygame.event.get():
          if event.type == pygame.QUIT:
             game.playing = False
             game.running = False
          elif event.type == pygame.KEYDOWN:
             game.run()

    def reset_screen_color(self, screen):
       screen.fill((255, 255, 255))

    def update_message(self, message, message1, message2, message3, rect_x, rect_y):
       self.text = self.font.render(message, True, (91, 0, 100))
       self.text_rect = self.text.get_rect()
       self.text_rect.center = (rect_x // 2, rect_y // 2)#cordenada

       self.text0 = self.font.render(message1, True, (73, 24, 220))
       self.text_rect0 = self.text0.get_rect()
       self.text_rect0.center = (rect_x // 2, 5*rect_y //8)#cordenada

       self.text1 = self.font.render(message2, True, (100, 0, 0))
       self.text_rect1 = self.text1.get_rect()
       self.text_rect1.center = (rect_x // 2, 3*rect_y // 4)#cordenada

       self.text2 = self.font.render(message3, True, (255, 0, 0))
       self.text_rect2 = self.text2.get_rect()
       self.text_rect2.center = (rect_x // 2, 7*rect_y // 8)