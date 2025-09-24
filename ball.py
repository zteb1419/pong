from utils import load_sprite, snd_pong

from pygame.math import Vector2
from pygame import Rect
import random
class Ball:
    def __init__(self):
        
        self.position = Vector2(random.randint(40, 760), random.randint(40, 560))
  
        self.velocity = Vector2(5, 5)
        self.sprite = load_sprite("tennis")
        self.pong_sound = snd_pong("pong")
        self.ping_sound = snd_pong("ping")
        

    def draw(self, surface):
        surface.blit(self.sprite, self.position)

    def move(self):
        if self.position.x > 800 - self.sprite.get_width() or self.position.x < 0:
            self.velocity.x *= -1
            self.ping_sound.play()
        if self.position.y < 0 or self.position.y > 600 - self.sprite.get_height():
            self.velocity.y *= -1
            self.ping_sound.play()
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

    def get_sprite_rect(self):
        return Rect(self.position.x, self.position.y, self.sprite.get_width(), self.sprite.get_height())
        
        
        
