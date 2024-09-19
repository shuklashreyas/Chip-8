class Chip8:
    def __init__(self):
        self.memory = [0] * 4096
        self.registers = [0] * 16
        self.index_register = 0
        self.PC = 0x200
        self.stack = []
        self.delay_timer = 0
        self.sound_timer = 0
        self.keys = [0] * 16

    def load_rom(self, file_path):
        with open(file_path, 'rb') as f:
            rom_data = f.read()
            for i, byte in enumerate(rom_data):
                self.memory[0x200 + i] = byte

    def fetch_opcode(self):
        return (self.memory[self.PC] << 8) | self.memory[self.PC + 1]

    def emulate_cycle(self):
        opcode = self.fetch_opcode()
        self.decode_and_execute(opcode)
        self.PC += 2

    def decode_and_execute(self, opcode):
        opcode_str = hex(opcode)
        print(f"Executing opcode: {opcode_str}")
        pass
