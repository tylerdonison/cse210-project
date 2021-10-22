"""image loader for the ghost, map, title, fingerprints, instrument screen, ghost types, pause screen
    """
from pathlib import Path

class Image_Loader:
    """ class for loading images into the game
    """
    def __init__(self):
        """Class Constructor
        """
        self.root = Path(__file__).parent
        self.map_path = self.root / "images" / "Apartment_3.0.json"
        self.ghost_front_path = self.root / "images" / "ghost_front_sprite.png"
        self.title_screen = self.root / "images" / "title_screen_v2.png"
        self.instruction_screen = self.root / "images" / "instruction_screen_controls_v2.png"
        self.ghost_types_screen = self.root / "images" / "ghost_types_screen.png"
        self.pause_screen = self.root / "images" / "pause_screen.png"
        
        
    def get_map_name(self):
        """gets the map name

        Returns:
            (self): map_path
        """
        return self.map_path

    def get_ghost_front_path(self):
        """gets ghost front path for ghost image

        Returns:
            self: ghost_front path to image
        """
        return self.ghost_front_path

    def get_title_screen(self):
        """ gets the title screen

        Returns:
            self: returns title_screen image
        """
        return self.title_screen
   
    def get_fingerprints(self):
        """gets fingerprints image

        Returns:
            self: fingerprints image
        """
        return self.fingerprints

    def get_instruction_screen(self):
        """get instruction screen for How to Play

        Returns:
            self: returns instruction screen
        """
        return self.instruction_screen

    def get_ghost_types_screen(self):
        """gets ghost types screen 

        Returns:
            self: returns screen with ghost types
        """
        return self.ghost_types_screen
    
    def get_pause_screen(self):
        """ gets pause screen

        Returns:
            self: returns pause screen
        """
        return self.pause_screen
