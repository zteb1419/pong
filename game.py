import pygame, sys
from ball import Ball
from paddle import Paddle
from utils import play_music, load_image
from pathlib import Path

class Pong:
    def __init__(self):
        pygame.init()
        play_music("gamemusic", 0.3)
        pygame.display.set_caption("Bouncing ball")
        self.screen:pygame.surface.Surface = pygame.display.set_mode(((800, 600)))
        self.background = load_image("background")
        self.ball = Ball()
        self.clock = pygame.time.Clock()
        self.paddle = Paddle(self.screen, 780, 200)
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        



    def main_loop(self):
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()
            self.clock.tick(60)

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.paddle.position.y > 0:
            self.paddle.position.y -= 5
        if keys[pygame.K_DOWN] and self.paddle.position.y < 520: 
            self.paddle.position.y += 5


    def _game_logic(self):
        ball_rect = self.ball.get_sprite_rect()
        paddle_rect = self.paddle.get_paddle_rect()
        
        
        if paddle_rect.colliderect(ball_rect):
            self.ball.pong_sound.play()
            self.ball.velocity.x *= -1
            self.ball.position.x -= self.ball.sprite.get_width()
            
            self.score += 1
            

        self.ball.move()
        
        

    def _draw(self):
        self.screen.fill('blue')
        self.screen.blit(self.background, (0, 0))
        
        
        self.ball.draw(self.screen)
        self.paddle.draw()
        rendered_font = self.font.render("Score: " + str(self.score), True, (255, 255, 0))
        self.screen.blit(rendered_font, (10, 10))
        #pygame.display.flip()
        pygame.display.update()