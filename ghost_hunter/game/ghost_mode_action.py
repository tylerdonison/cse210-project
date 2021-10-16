"""This module is in charge of controlling the actions of the ghost"""
import random
from game import constants

class Action_Mode():
    """This is the class that controls the actions of the ghost while they are not hunting.

    Stereotype: Service Provider
    """
    def __init__(self):
        """The class constructor

        Args:
            self (Action_Mode): an instance of Action Mode
        """
        
        self.possible_objects = {f"{constants.ROOM_LIST[0]}" : constants.DINNING_INTERACTIONS, 
        f'{constants.ROOM_LIST[1]}' : constants.BEDROOM_INTERACTIONS,
        f'{constants.ROOM_LIST[2]}' : constants.BATHROOM_INTERACTIONS}

        self.interaction_types = {"ghost_type1":["fingerprints"]}

    def cause_ghost_interaction(self):
        """This method causes there to be a ghost interaction in a randomly selected room on a random object
        in the room. The ghost interaction is randomly selected from a list containing the possible interactions for 
        the given type of ghost
        Args: 
            self(GhostInteraction): an instance of GhostInteraction
        """
        #choose a room, and object
        room = random.choice(constants.ROOM_LIST)
        possible_objects_for_room = self.possible_objects[room]
        object = random.choice(possible_objects_for_room)

        #choose the type of interaction
        ghost = "ghost_type1" #We would replace this later and pass in an argument
        possible_interactions = self.interaction_types[ghost]
        interaction = random.choice(possible_interactions)

        if interaction == "fingerprints":
            self.place_fingerprints(room, object)


    def place_fingerprints(self, room, object):
        """This method replaces an object in a room, with an object that has fingerprints on it from a ghost
        Args:
            self(GhostInteraction): an instance of GhostInteraction
            Room: The room that the fingerprints will be in
            Object: The object that will have the fingerprints placed on them
        """
        #at this point we need to find a way to replace the previous image of the object with a new one
        pass
