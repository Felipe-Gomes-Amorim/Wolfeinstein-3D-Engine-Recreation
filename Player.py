from Settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = player_pos
        self.angle = player_angle

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0 
        speed = player_speed * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos
       

        self.check_wall_collision(dx, dy)

        #if keys[pg.K_LEFT]:
        #    self.angle -= player_rot_speed * self.game.delta_time
        #if keys[pg.K_RIGHT]:
        #   self.angle += player_rot_speed * self.game.delta_time
        self.angle %= math.tau
        
    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self , dx, dy):
        scale = player_size_scale / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx 
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy


    def draw(self):
       # pg.draw.line(self.game.screen, 'yellow' ,(self.x * 100 , self.y * 100),
        #            (self.x * 100 + largura * math.cos(self.angle),
         #            self.y * 100 + largura * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15 )
    
    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < mouse_border_left or mx > mouse_border_right:
            pg.mouse.set_pos([half_widht, half_height])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-mouse_max_rel, min(mouse_max_rel, self.rel))
        self.angle += self.rel * mouse_sensisitivity * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)

        