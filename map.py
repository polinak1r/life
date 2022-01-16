from time import time
from config import *
import random as rnd, pygame


class Map:
    def __init__(self, app, map_size, tile_size, update_interval, loop, random_fill=0.1):
        self.update_interval = update_interval
        self.loop = loop
        self.tile_size = tile_size
        self.update_time = time() + 2
        self.map_size = self.width, self.height = map_size
        self.state = [[rnd.random() <= random_fill for y in range(self.height)] for x in range(self.width)]
        self.update_tiles = []
        self.app = app
        self._draw()

    def update(self):
        if self.update_time > time(): return
        self._update()
        self.update_time = time() + self.update_interval

    def get_neighbours(self, x, y):
        dx = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        cnt = 0
        for d in dx:
            x1, y1 = x + d[0], y + d[1]
            if self.loop:
                x1 = (x1 + self.width) % self.width
                y1 = (y1 + self.height) % self.height
            if not (0 <= x1 < self.width and 0 <= y1 < self.height): continue
            cnt += self.state[x1][y1]
        return cnt

    def _update(self):
        self.update_tiles = []
        for x in range(self.width):
            for y in range(self.height):
                if self.state[x][y] and not (2 <= self.get_neighbours(x, y) <= 3):
                    self.update_tiles.append((x, y))
                if not self.state[x][y] and self.get_neighbours(x, y) == 3:
                    self.update_tiles.append((x, y))

    def _draw(self):
        for x in range(self.width):
            for y in range(self.height):
                color = live_color if self.state[x][y] else dead_color
                rect = (x * self.tile_size, y * self.tile_size, (x + 1) * self.tile_size, (y + 1) * self.tile_size)
                pygame.draw.rect(self.app.screen, color, rect)

    def draw(self):
        for x, y in self.update_tiles:
            self.state[x][y] = not self.state[x][y]
            color = live_color if self.state[x][y] else dead_color
            rect = (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
            pygame.draw.rect(self.app.screen, color, rect)
        self.update_tiles = []
