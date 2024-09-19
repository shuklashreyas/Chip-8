import pygame
from chip8 import Chip8
from display import Display
from input import InputHandler
from sound import Sound
from rom import load_rom


def main():
    pygame.init()
    clock = pygame.time.Clock()

    chip8 = Chip8()
    display = Display()
    input_handler = InputHandler()
    sound = Sound()

    rom_data = load_rom("path_to_rom.ch8")
    chip8.load_rom(rom_data)

    while True:
        chip8.emulate_cycle()
        input_handler.handle_input()
        display.render()
       
        if chip8.delay_timer > 0:
            chip8.delay_timer -= 1
        if chip8.sound_timer > 0:
            chip8.sound_timer -= 1
            if chip8.sound_timer == 0:
                sound.play_sound()

        clock.tick(60) 


if __name__ == "__main__":
    main()
