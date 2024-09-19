def load_rom(filepath):
    with open(filepath, 'rb') as f:
        return f.read()
