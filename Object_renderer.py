import pygame as pg
from Settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures  = self.load_wall_textures()
        self.sky_image = self.get_texture('Resources/Textures/Sky.png', (largura, half_height))
        self.sky_offset = 0
    
    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        self.sky_offset =  (self.sky_offset + 4.0 * self.game.player.rel) % largura
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + largura, 0))
        # floor
        pg.draw.rect(self.screen, floor_color, (0, half_height, largura, altura))


    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(texture_size, texture_size)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('Resources/Textures/1.png'),
            2: self.get_texture('Resources/Textures/2.png'),
            3: self.get_texture('Resources/Textures/3.png'),
            4: self.get_texture('Resources/Textures/4.png'),

        }