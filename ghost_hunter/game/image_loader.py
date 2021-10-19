from pathlib import Path

class Image_Loader:
    def __init__(self):
        self.root = Path(__file__).parent
        self.map_path = self.root / "images" / "Apartment_3.0.json"
        self.ghost_front_path = self.root / "images" / "ghost_front_sprite.png"
        self.title_screen = self.root / "images" / "title_screen.png"
        
        
    def get_map_name(self):
        return self.map_path

    def get_ghost_front_path(self):
        return self.ghost_front_path

    def get_title_screen(self):
        return self.title_screen

