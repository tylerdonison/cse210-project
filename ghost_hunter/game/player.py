"""This is the class in charge of the player.
"""

from PIL.Image import Image
import arcade
from arcade.sprite import Sprite
from game.constants import CHARACTER_SCALING
from game.constants import PLAYER_MOVEMENT_SPEED, PLAYER_START_X, PLAYER_START_Y
from threading import Timer
from game.image_loader import Image_Loader

class Player(arcade.Sprite):
    """The Player class holds information about the player of the game.

    Stereotype: Information Holder

    Attributes:
        sanity (int): The sanity of the player.
    """
    
    def __init__(self):
        """The class constructor

        Args:
            self (Player): An instance of Player
        """
        super().__init__()
        
        main_image = Image_Loader().get_player_front()
        
        self.sprite = arcade.Sprite(main_image, .75)
        self.sprite._set_center_x(PLAYER_START_X)
        self.sprite._set_center_y(PLAYER_START_Y)
        
        self.sanity = 100
        self.has_instrument = False
        self.index_of_instrument = None
        
        timer = Timer(5.0, self.decrease_sanity)
        timer.start()
        self.cur_texture = 0
        self.character_direction = 1 #0 is up, 1 is down, 2 is right, 3 is left
        self.player_animations = Image_Loader().get_player_animations()
        self.player_idle_animations =       [arcade.load_texture(self.player_animations[0]), 
                                             arcade.load_texture(self.player_animations[3]), 
                                             arcade.load_texture(self.player_animations[6]),
                                             arcade.load_texture(self.player_animations[9])]
        self.player_walk_up_animations =    [arcade.load_texture(self.player_animations[1]), 
                                             arcade.load_texture(self.player_animations[2])]
        self.player_walk_down_animations =  [arcade.load_texture(self.player_animations[4]), 
                                             arcade.load_texture(self.player_animations[5])]
        self.player_walk_right_animations = [arcade.load_texture(self.player_animations[7]), 
                                             arcade.load_texture(self.player_animations[8])]
        self.player_walk_left_animations =  [arcade.load_texture(self.player_animations[10]), 
                                             arcade.load_texture(self.player_animations[11])]
        self.texture = self.player_idle_animations[1]
        self.walking_animations = [self.player_walk_up_animations, self.player_walk_down_animations,
                                self.player_walk_right_animations, self.player_walk_left_animations]
        #arcade.load_textures()
    
    def update_animation(self, delta_time: float = 1 / 60):

        """Updates the animation of the player

        Args:
            self (Player): An instance of Player
            delta_time (float): The delta time of the animation

        """
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.player_idle_animations[self.character_direction]
        
        self.cur_texture += 1
        if self.cur_texture > 1:
            self.cur_texture = 0
        walking_animation_list = self.walking_animations[self.character_direction]
        self.texture = walking_animation_list[self.cur_texture]
    
    def decrease_sanity(self):

        """Decreases the player's sanity

        Args:
            self (Player): An instance of Player
        """
        self.sanity -= 1
        if self.sanity > 0:
            timer = Timer(2.0, self.decrease_sanity)
            timer.start()

    def set_instrument(self, index):
        """Sets the instrument the player holds

        Args:
            self (Player): An instance of Player
            index (int): the index of the instrument

        """
        self.has_instrument = True
        self.index_of_instrument = index
