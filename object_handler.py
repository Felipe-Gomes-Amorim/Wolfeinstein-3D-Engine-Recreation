from sprite_object import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path ='Resources/Sprites/'
        add_sprite = self.add_sprite

        #sprite map
        add_sprite(SpriteObject(game)) 
        add_sprite(SpriteObject(game, path=self.static_sprite_path +'celular.png' , pos=(1.5 , 3)))

    def update (self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)