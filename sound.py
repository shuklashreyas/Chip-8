import pygame


class Sound:
    def __init__(self):
        pygame.mixer.init()

    def play_sound(self):
        beep = pygame.mixer.Sound('beep.wav')
        beep.play()
