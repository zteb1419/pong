import pygame

from pygame.math import Vector2

class Paddle:
    WIDTH:int = 20
    HEIGHT:int = 80
    def __init__(self, surface, posX, posY):
        self.surface = surface
        self.position = Vector2(posX, posY)
        
        
       

    def get_paddle_rect(self) -> pygame.Rect:
        return pygame.Rect(self.position.x, self.position.y, Paddle.WIDTH, Paddle.HEIGHT)
        

    def draw(self) -> None:
        pygame.draw.rect(self.surface, (255, 0, 0), self.get_paddle_rect(), 0, 5)
        
        




        
