import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_1

from game.components.bullets.bullet import Bullet

class Enemy(Sprite):
    # Posición inicial del enemigo en el eje Y
    Y_POS = 20
    # Lista de posiciones iniciales del enemigo en el eje X
    X_POS_LIST = [50, 150, 250, 350, 450, 550, 300, 100, 258, 400]
    # Velocidad de movimiento horizontal del enemigo
    SPEED_X = 5
    # Velocidad de movimiento vertical del enemigo
    SPEED_Y = 1
    # Dirección de movimiento horizontal del enemigo
    MOD_X = {0:'left', 1:'right'}

    def __init__(self):
        # Establecer la imagen del enemigo
        self.image = ENEMY_1
        # Escalar la imagen del enemigo
        self.image = pygame.transform.scale(self.image, (40, 60))
        # Establecer el rectángulo del enemigo
        self.rect = self.image.get_rect()
        # Establecer la posición inicial del enemigo
        self.rect.x = random.choice(self.X_POS_LIST)
        # Establecer la posición inicial del enemigo
        self.rect.y = self.Y_POS
        # Establecer el tipo de sprite
        self.type = 'enemy'

        # Establecer la dirección de movimiento horizontal del enemigo
        self.mod_x = random.choice(self.MOD_X)
        # Establecer la velocidad de movimiento horizontal del enemigo
        self.speed_x = self.SPEED_X
        # Establecer la velocidad de movimiento vertical del enemigo
        self.speed_y = self.SPEED_Y
        # Establecer el número de fotogramas antes de cambiar la dirección de movimiento horizontal del enemigo
        self.move_x_for = random.randint(30, 100)
        # Contador de fotogramas para cambiar la dirección de movimiento horizontal del enemigo
        self.index = 0
        # Tiempo de espera antes de disparar
        self.shooting_time = random.randint(30, 50)

    def change_movemet_in_x(self):
        # Incrementar el contador de fotogramas
        self.index += 1
        # Verificar si el contador ha alcanzado el número de fotogramas antes de cambiar la dirección de movimiento horizontal del enemigo
        if(self.index >= self.move_x_for and self.mod_x == 'right') or (self.rect.x >= SCREEN_WIDTH - 40 ):
            # Cambiar la dirección de movimiento horizontal del enemigo si se está moviendo hacia la derecha y ha alcanzado el borde derecho de la pantalla
            self.mod_x = 'left'
        elif(self.index >= self.move_x_for and self.mod_x == 'left') or (self.rect.x <= 10):
            # Cambiar la dirección de movimiento horizontal del enemigo si se está moviendo hacia la izquierda y ha alcanzado el borde izquierdo de la pantalla
            self.mod_x = 'right'
        # Reiniciar el contador de fotogramas si ha alcanzado el número de fotogramas antes de cambiar la dirección de movimiento horizontal del enemigo
        if(self.index >= self.move_x_for):
            self.index = 0

    def update(self, ships, game):
        # Actualizar la posición del enemigo en cada fotograma
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)

        if self.mod_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movemet_in_x()
        elif self.mod_x == 'right':
            self.rect.x += self.speed_x
            self.change_movemet_in_x()
        
        # Eliminar el enemigo del juego cuando llega al borde inferior de la pantalla
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time = random.randint(30, 50)

    def draw(self, screen):
        # Dibujar la imagen del enemigo en la pantalla
        screen.blit(self.image, (self.rect.x, self.rect.y))