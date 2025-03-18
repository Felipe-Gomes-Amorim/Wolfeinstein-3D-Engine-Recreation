import pygame as pg
import sys
from Settings import *
from map import *
from Player import *
from Raycasting import *
from Object_renderer import *
from sprite_object import *
from object_handler import *
import asyncio


class Game:
    def __init__(self):
        #inicializa o pygame, o tamanho da tela e o clock
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(Resolution)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        pg.mouse.set_pos((400, 300))
        pg.event.set_grab(True)
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)

    def update(self):
        #atualiza tudo de acordo com o fps
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def draw(self):
        #pinta a tela de preto toda vez
        #self.screen.fill('black')
        self.object_renderer.draw()
        #self.map.draw()
        #self.player.draw()
    
    def check_events(self):
        #checa por eventos, no caso teclas apertadas ou etc...

       
        for event in pg.event.get():
            #fecha o aplicativo
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    async def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

            # Atualiza o relógio do jogo com asyncio.sleep
            await asyncio.sleep(1 / FPS)

async def main():
    game = Game()
    await game.run()

if __name__ == '__main__':
    game = Game()
    asyncio.run(main())