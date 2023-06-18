import pygame

from game.components.enemies.enemy_weak.enemy import Enemy
from game.utils.constants import SHIELD_TYPE, SOUND_2

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.Sound = pygame.mixer.Sound(SOUND_2)

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.playing = False
                    pygame.time.delay(1000)
                    game.death_count.update()
                break
        
        for bullet in self.bullets:
            bullet.update(self.bullets)
            # condicional para verificar que el bullet colisione con el enemigo
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    game.score.update()
                    
                    

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' and len(self.bullets) < 2:
            self.bullets.append(bullet)
            self.Sound.play(1)

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []