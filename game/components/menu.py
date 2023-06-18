import pygame

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_STYLE


class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

    def __init__(self,screen):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE, 30)

    def handle_events_to_menu(self,game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            if event.type == pygame.KEYDOWN:
                game.run()
    
    def update(self,game):
        pygame.display.update()
        self.handle_events_to_menu(game)
    
    def draw(self,screen, message,x=HALF_SCREEN_WIDTH,y=HALF_SCREEN_HEIGHT, color = (0,0,0)):
        text = self.font.render(message, True, color)
        text_rect = text.get_rect()
        text_rect.center = (x,y)
        screen.blit(text, text_rect)

    def reset_screen_collor(self,screen):
        screen.fill((255,255,255))