import pygame as pg


class Display:
    def __init__(self):
        self.screen = [[0] * 64 for _ in range(32)]

    def clear(self):
        self.screen = [[0] * 64 for _ in range(32)]

    def draw_sprite(self, x, y, sprite_data):
        for i in range(len(sprite_data)):
            for j in range(8):
                pixel = (sprite_data[i] >> (7 - j)) & 1
                self.screen[y + i][x + j] ^= pixel

    def render(self):
        pg.init()
        screen = pg.display.set_mode((640, 320))
        pg.display.set_caption("Chip8 Emulator")
        screen.fill((0, 0, 0))
        for i in range(32):
            for j in range(64):
                if self.screen[i][j]:
                    pg.draw.rect(screen, (255, 255, 255),
                                 (j * 20, i * 10, 20, 10))
        pass
