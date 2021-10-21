"""This is the class in charge of the player.
"""

import arcade
from arcade.sprite import Sprite
from game.constants import CHARACTER_SCALING
from game.constants import PLAYER_MOVEMENT_SPEED, PLAYER_START_X, PLAYER_START_Y
from game.entity import Entity
from threading import Timer

class Player(Entity):
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
        Entity.__init__(self)
        Entity.setup(
            self,  ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", PLAYER_START_X, PLAYER_START_Y)
        self.sanity = 100
        self.has_instrument = False
        self.instrument = Sprite()
        self.index_of_instrument = None

        #needs to be set up to be lower, but it will trigger hunting mode too fast
        #while we are still working on it
        timer = Timer(40.0, self.decrease_sanity)
        timer.start()
    
    def decrease_sanity(self):
        self.sanity -= 5
        if self.sanity > 0:
            timer = Timer(40.0, self.decrease_sanity)
            timer.start()

    def set_instrument(self, instrument, index):
        self.has_instrument = True
        self.index_of_instrument = index
        self.instrument = instrument