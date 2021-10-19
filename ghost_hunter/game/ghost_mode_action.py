"""This module is in charge of controlling the actions of the ghost"""
import random
from game import constants
import arcade
from game.image_loader import Image_Loader

class Action_Mode():
    """This is the class that controls the actions of the ghost while they are not hunting.

    Stereotype: Service Provider
    """
    def __init__(self, ghost_type):
        """The class constructor

        Args:
            self (Action_Mode): an instance of Action Mode
            ghost_type (string): The type of ghost for the current game
        """
        self.room = random.choice(constants.ROOM_LIST)
        self.ghost_type = ghost_type
        self.emf_position = [0,0]
        self.freezing_position = [0,0]
        self.interaction_types = {"ghost_type1":["fingerprints"], "ghost_type2":['emf'], "ghost_type3":["freezing"]}

    def cause_ghost_interaction(self):
        """This method causes there to be a ghost interaction in a randomly selected room on a random object
        in the room. The ghost interaction is randomly selected from a list containing the possible interactions for 
        the given type of ghost

        Args: 
            self (Action_Mode): an instance of Action Mode
        """
        #choose a room, and object
        possible_objects_for_room = constants.INTERACTIONS_DICTIONARY[self.room]
        target_object = random.choice(possible_objects_for_room)

        #choose the type of interaction
        ghost = "ghost_type1" #We would replace this later and pass in an argument
        possible_interactions = self.interaction_types[ghost]
        interaction = random.choice(possible_interactions)

        if interaction == "fingerprints":
            self.place_fingerprints(target_object)
        if interaction == "emf":
            self.set_emf()
        if interaction == "freezing":
            self.set_freezing()


    def place_fingerprints(self, target_object):
        """This method replaces an object in a room, with an object that has fingerprints on it from a ghost
        Args:
            self (Action_Mode): an instance of Action Mode
            Room: The room that the fingerprints will be in
            Object: The object that will have the fingerprints placed on them
        """
        
        object_x = constants.OBJECT_COORDINATES[target_object][0]
        object_y = constants.OBJECT_COORDINATES[target_object][1]
        path = Image_Loader.get_fingerprints()
        arcade.Sprite(path,1,object_x, object_y)

    def set_emf(self,target_object):
        """Sets the location of an emf point

        Args:
            self (Action_Mode): an instance of Action Mode
            target_object: the name of the object where the emf will be emitted from
        """
        
        emf_x = constants.OBJECT_COORDINATES[target_object][0]
        emf_y = constants.OBJECT_COORDINATES[target_object][1]
        self.emf = [emf_x, emf_y]
        
    def set_freezing(self, target_object):
        """Sets the location of an emf point

        Args:
            self (Action_Mode): an instance of Action Mode
            target_object: the name of the object where the emf will be emitted from
        """

        freezing_x = constants.OBJECT_COORDINATES[target_object][0]
        freezing_y = constants.OBJECT_COORDINATES[target_object][1]
        self.freezing = [freezing_x, freezing_y]
        

    def adjust_temp_reading(self, player):
        """Adjusts the temperature reading. It will decrease as the player gets closer and get smaller as the player gets 
        farther away.

        Args:
            self (Action_Mode): an instance of Action Mode
            player (Player): an instance of the player class

        Returns:
            (float) The termperature reading to display to the user
        """
        if self.freezing_position == [0,0]:
            temperature_reading = float(random.randint(60-70)) + random.random()
        else:
            x_of_player = player.sprite._get_center_y()
            y_of_player = player.sprite._get_center_y()
            x_of_freezing = self.freezing[0]
            y_of_freezing = self.freezing[1]
            distance = arcade.get_distance(x1=x_of_player, y1=y_of_player, x2=x_of_freezing, y2=y_of_freezing)
            temperature_reading = 70 -  70 / distance #The constant value will probably need adjusted later

        return temperature_reading

    def adjust_emf_reading(self,player):
        """Adjusts the EMF reading. It will increase as the player gets closer and get smaller as the player gets 
        farther away.

        Args:
            self (Action_Mode): an instance of Action Mode
            player (Player): an instance of the player class

        Returns:
            (float) The emf reading to display to the user
        """
        if self.freezing_position == [0,0]:
            temperature_reading = float(random.randint(20-30)) + random.random()
        else:
            x_of_player = player.sprite._get_center_y()
            y_of_player = player.sprite._get_center_y()
            x_of_emf = self.emf[0]
            y_of_emf = self.emf[1]
            distance = arcade.get_distance(x1=x_of_player, y1=y_of_player, x2=x_of_emf, y2=y_of_emf)
            emf_reading = 20 + 100 / distance #The constant value will probably need adjusted later

        return emf_reading

