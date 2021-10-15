"""This is the class in charge of the player.
"""

import arcade
from game.constants import CHARACTER_SCALING
from game.constants import PLAYER_MOVEMENT_SPEED, PLAYER_START_X, PLAYER_START_Y
from game.entity import Entity

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

