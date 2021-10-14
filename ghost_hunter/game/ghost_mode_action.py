import random
import constants

class Action_Mode():
    def __init__(self):
        """The class constructor
        Stereotype: Service Provider
        Args:
            self (Action_Mode): an instance of Action Mode
        """
        
        self.possible_objects = {f'{constants.ROOM_LIST[0]}' : constants.DINNING_INTERACTIONS, 
        f'{constants.ROOM_LIST[1]}' : constants.BEDROOM_INTERACTIONS,
        f'{constants.ROOM_LIST[2]}' : constants.BATHROOM_INTERACTIONS}

        self.interaction_types = {"ghost_type1":["fingerprints"]}
    
    #will only hunt if player's sanity is below 50, when hunt check passes, it will activate hunt phase.

    def Hunt_Check(sanity):
        """Checks to see if the ghost will hunt the player. There is a 1 in 20 chance of being hunted if they have 100 sanity
        and a 1 in 1 chance if their sanity gets to 5

        Args:
            sanity (int): The ammount of sanity that the player has.

        """

        #This ensures that the chance of being hunted will never be greater than a 1 in 1 chance (prevent bugs)
        if sanity < 5:
            sanity = 5 #Remember that this won't change sanity globally. Just don't pass in sanity as a number instead of accessing it through an object

        
        chance_of_being_hunted_inverse = sanity / 5
        round(chance_of_being_hunted_inverse) #ensures that the chance of being hunted will be an int

        #creates a list from 1 to the inverse of the chance of being hunted. (A greater number is better for the player). Then randomly chooses a number
        #from the list. If it is a one, they will be hunted. Chances of having a 1 increase with a smaller list.
        chance_list = []
        for i in range(chance_of_being_hunted_inverse):
            chance_list.append(i + 1)

        random_number_in_chance_list = random.choice(chance_list)
        if random_number_in_chance_list == 1:
            ghost_hunt_mode = True #This will probably need to be changed to an object that is passed in

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
            self.place_fingerprints(self, room, object)


    def place_fingerprints(self, room, object):
        """This method replaces an object in a room, with an object that has fingerprints on it from a ghost
        Args:
            self(GhostInteraction): an instance of GhostInteraction
            Room: The room that the fingerprints will be in
            Object: The object that will have the fingerprints placed on them
        """
        #at this point we need to find a way to replace the previous image of the object with a new one
        pass
