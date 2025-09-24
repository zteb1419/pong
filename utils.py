from pygame.image import load
from pygame.mixer import music, Sound

from pathlib import Path

def load_sprite(name, with_aplpha = True):
    filename = Path(__file__).parent/Path("assets/sprites/" + name + ".png")
    sprite = load(filename.resolve())
    if with_aplpha:
        return sprite.convert_alpha()
    return sprite.convert

def play_music(name, volume) -> None:
    filename = Path(__file__).parent/Path("assets/sounds/" + name + ".mp3")
    music.load(filename)
    music.play(-1)
    music.set_volume(volume)

def snd_pong(name:str) -> Sound:
    filename = Path(__file__).parent/Path("assets/sounds/" + name + ".mp3")
    snd:Sound = Sound(filename)
    return snd

def load_image(name):
    filename = Path(__file__).parent/Path("assets/sprites/" + name + ".png")
    img = load(filename.resolve())
    return img.convert()
    
