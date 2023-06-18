import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, DEFAULT_TYPE, THUNDER

from game.components.bullets.bullet import Bullet


class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 40
    Y_POS = 500

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.has_power_up = False
        self.power_time_up = 0
        self.power_up_type = DEFAULT_TYPE
        self.speed_boost = False


    def move_left(self ):
        if self.rect.x > 0:
            if self.speed_boost == True:
                self.rect.x -= 20
            else:
                self.rect.x -= 10
        elif self.rect.x == 0:
            self.rect.x = SCREEN_WIDTH - 40
    
    def move_right(self):
        if self.rect.x < SCREEN_WIDTH - 40:
            if self.speed_boost == True:
                self.rect.x += 20
            else:
                self.rect.x += 10
        elif self.rect.x == SCREEN_WIDTH - 40:
            self.rect.x = 0
    
    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            if self.speed_boost == True:
                self.rect.y -= 20
            else:
                self.rect.y -= 10

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            if self.speed_boost == True:
                self.rect.y += 20
            else:
                self.rect.y += 10

    def update(self, user_input, game):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_SPACE]:
            self.shoot(game.bullet_manager)
        
    def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def reset(self):
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.speed_boost = False

    # metodo para activar imagen
    def set_image(self, size=(40,60), image = SPACESHIP):
        # actualizamos la imagen
        self.image = image
        #escalamos la imagen
        self.image = pygame.transform.scale(self.image, size)

    def apply_speed_boost(self):
        self.speed_boost = True

 