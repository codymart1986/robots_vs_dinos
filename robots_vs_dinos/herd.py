class Herd:
    def __init__(self):
        self.dino_herd = []

    def add_dino(self, dino):
        self.dino_herd.insert(0,dino)