from pathlib import Path

class Image_Loader:
    def __init__(self):
        self.root = Path(__file__).parent
        self.map_path = self.root / "images" / "Apartment_3.0.json"
        self.ghost_front_path = self.root / "images" / "ghost_front_sprite.png"
        self.title_screen = self.root / "images" / "title_screen_v2.png"
        self.instruction_screen = self.root / "images" / "instruction_screen_controls_v2.png"
        self.ghost_types_screen = self.root / "images" / "ghost_types_screen.png"
        self.pause_screen = self.root / "images" / "pause_screen.png"
        self.fingerprints = self.root / "images" / "fingerprints.png"

        
    def get_map_name(self):
        return self.map_path

    def get_ghost_front_path(self):
        return self.ghost_front_path

    def get_title_screen(self):
        return self.title_screen

    def get_instruction_screen(self):
        return self.instruction_screen

    def get_ghost_types_screen(self):
        return self.ghost_types_screen
    
    def get_pause_screen(self):
        return self.pause_screen

    def get_fingerprints(self):
        return self.fingerprints
