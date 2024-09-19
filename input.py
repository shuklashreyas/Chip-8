import pygame


class InputHandler:
    def __init__(self):
        self.keys = [0] * 16

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # Map keyboard keys to CHIP-8 keys
                if event.key == pygame.K_1:
                    self.keys[0x1] = 1
            elif event.type == pygame.KEYUP:
                # Reset keys when released
                if event.key == pygame.K_1:
                    self.keys[0x1] = 0
