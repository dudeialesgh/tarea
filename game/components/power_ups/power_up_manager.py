import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.speed_power_up import SpeedPowerUp
from game.utils.constants import SHIELD_TYPE, SHIELD, SPACESHIP_SHIELD, THUNDER_TYPE, SPACESHIP

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000,10000)
        self.duration = random.randint(3,5)

    def generate_power_up(self):
        # Genera un power-up aleatorio (escudo o aumento de velocidad)
        power_up_type = random.choice([Shield, SpeedPowerUp])
        power_up = power_up_type()
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)
    
    def update(self, game):
        # capturo el tiempo
        current_time = pygame.time.get_ticks()
        # si el power up esta vacio y el tiempo actual es mayor al tiempo de aparicion
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        # itero en los power ups
        for power_up in self.power_ups:
            current_time = pygame.time.get_ticks()
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()

                if isinstance(power_up, Shield):
                    game.player.power_up_type = SHIELD_TYPE
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
                elif isinstance(power_up, SpeedPowerUp):
                    game.player.power_up_type = THUNDER_TYPE
                    game.player.apply_speed_boost()
                    game.player.set_image((40, 60), SPACESHIP)

                game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                self.power_ups.remove(power_up)
                game.player.has_power_up = True


    def draw(self, screen):
        # dibujamos iterando en los power ups
        for power_up in self.power_ups:
            # ya el mismo se dibuja hacemos uso del metodo, enviando la pantalla
            power_up.draw(screen)
        
    # reseteamos 
    def reset(self):
        # capturamos el tiempo
        now = pygame.time.get_ticks()
        # limpiamos la lista de power ups
        self.power_ups = []
        # generamos nuevamente cuando se reinicie
        self.when_appears =  random.randint(5000,10000)
