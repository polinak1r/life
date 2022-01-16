import pygame
from map import Map
from config import *


class App:
    def __init__(self):
        self.resolution = self.width, self.height = (tile_size * map_size[0], tile_size * map_size[1])
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.map = Map(self, map_size, tile_size, (1 / max(sim_speed, 0.001)), loop, random_fill)

    def update(self):
        self.map.update()

    def draw(self):
        self.map.draw()
        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.update()
            self.draw()

            self.clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    app = App()
    app.run()
