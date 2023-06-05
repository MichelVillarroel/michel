import pygame

import random
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, ROCK_1, ROCK_2, ROCK_3, ROCK_4, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE, GAME_OVER, SCREEN_WIDTH

from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.menu import Menu



class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()#inicia music
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.death_count = 0
        self.score = 0
        self.score_highest = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()  
        self.bullet_manager = BulletManager()
        self.power_up_manager = PowerUpManager()
        self.menu = Menu('Press any button to start....', self.screen)
        self.lives = 0# Añadir atributo para almacenar las vidas del jugador
        
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.score = 0
        self.enemy_manager.reset()
        self.bullet_manager.reset()
        pygame.mixer.music.load("sounds/music.mp3")#cargar
        pygame.mixer.music.play()#reproducir
        # Game loop: events - update - draw
        self.reset()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.lives = self.player.lives  # Actualizar el contador de vidas del jugador
       # pygame.display.quit()
        #pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self) 
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.draw_score()
        self.draw_rock()#dibjar rocas
        pygame.display.update()
        #pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2

        self.menu.reset_screen_color(self.screen)
        self.print_menu_elements(self.death_count)


        icon = pygame.transform.scale(ICON, (80, 120))
        self.screen.blit(icon, (half_screen_width -50, half_screen_height -150))

        if self.death_count >0 :

          game_over = pygame.transform.scale(GAME_OVER, (300, 150))
          self.screen.blit(game_over, (half_screen_width -150, half_screen_height -250))

        self.menu.draw(self.screen)
        self.menu.update(self)

    def print_menu_elements(self, death_count):
        if self.score > self.score_highest:
            self.score_highest = self.score
        if self.death_count >0 :
            puntaje = 'Your Score: ' + str(self.score)
            muerto = 'Total Deaths: ' + str(self.death_count) 
            titulo = 'Press any key to restart ' 
            puntaje_alto = "Highest Score: " + str(self.score_highest)
            self.menu.update_message(titulo, puntaje, puntaje_alto, muerto, rect_x = SCREEN_WIDTH  , rect_y = SCREEN_HEIGHT )#

    def update_score(self):
        self.score += 1

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

        lives_text = font.render(f'HEART: {self.player.lives}', True, (255, 255, 255))
        lives_rect = lives_text.get_rect()
        lives_rect.topleft = (20, 20)
        self.screen.blit(lives_text, lives_rect)

    def reset(self):
        self.score = 0
        self.enemy_manager.reset()
        self.bullet_manager.reset()
        self.player.reset()
        self.power_up_manager.reset()
        self.lives = self.player.lives

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks())/1000, 2)

            if time_to_show >= 0:
                self.menu.draw_shield(self.screen, f'{self.player.power_up_type.capitalize()} is enabled for {time_to_show} seconds')
                #self.menu.draw(self.screen, f'{self.player.power_up_type.capitalize()} is enable for {time_to_show} seconds', 540, 50, (255, 255, 255))
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()

    def draw_rock(self):
        rock_images = [ROCK_1, ROCK_2, ROCK_3, ROCK_4]
        for rock_image in rock_images:
            rock_x = random.randint(0, SCREEN_WIDTH - rock_image.get_width())
            rock_y = random.randint(0, SCREEN_HEIGHT - rock_image.get_height())
            self.screen.blit(rock_image, (rock_x, rock_y))