"""This module is in charge of controlling the actions of the ghost"""
import random
from game import constants
import arcade
from game.image_loader import Image_Loader


class Action_Mode():
    """This is the class that controls the actions of the ghost while they are not hunting.

    Stereotype: Service Provider
    """
    def __init__(self, ghost_type, room_name):
        """The class constructor

        Args:
            self (Action_Mode): an instance of Action Mode
            ghost_type (string): The type of ghost for the current game
        """

        self.room = room_name
        self.ghost_type = ghost_type
        print(self.ghost_type)
        self.emf_position = [0,0]
        self.freezing_position = [0,0]
        self.interaction_types = {"poltergeist":["fingerprints","emf"], "wraith":['emf',"writing"], "demon":["writing", "fingerprints"]}      
        self.possible_objects = {f"{constants.ROOM_LIST[0]}": constants.INTERACTIONS_DICTIONARY["Dining Room"],
                                 f'{constants.ROOM_LIST[1]}': constants.INTERACTIONS_DICTIONARY["Bedroom"],
                                 f'{constants.ROOM_LIST[2]}': constants.INTERACTIONS_DICTIONARY["Bathroom"]}
        self.emf_reading = 1
        self.book_location = [0,0]
        self.writing_already = False

    def cause_ghost_interaction(self, scene,book, instruments_list):
        """This method causes there to be a ghost interaction in a randomly selected room on a random object
        in the room. The ghost interaction is randomly selected from a list containing the possible interactions for 
        the given type of ghost

        Args: 
            self (Action_Mode): an instance of Action Mode
            ghost_type (str): The type of ghost
            scene (obj): The scene object
        """
        #choose a room, and object
        possible_objects_for_room = constants.INTERACTIONS_DICTIONARY[self.room]
        target_object = random.choice(possible_objects_for_room)

        #choose the type of interaction
        possible_interactions = self.interaction_types[self.ghost_type]
        interaction = random.choice(possible_interactions)

        if interaction == "fingerprints":
            self.place_fingerprints(target_object,scene)
        if interaction == "emf":
            self.set_emf(target_object)
        if interaction == "writing":
            self.place_writing(book, instruments_list, scene)
        if interaction == "freezing":
            self.set_freezing(target_object)


    def place_fingerprints(self, target_object, scene):
        """This method replaces an object in a room, with an object that has fingerprints on it from a ghost
        Args:
            self (Action_Mode): an instance of Action Mode
            target_object: The object that will have the fingerprints placed on them
            scene: The scene object
        """
        
        object_x = constants.OBJECT_COORDINATES[target_object][0]
        object_y = constants.OBJECT_COORDINATES[target_object][1]
        path = Image_Loader().get_fingerprints()
        
        self.fingerprints = arcade.Sprite(path,center_x=object_x, center_y=object_y)
        scene.add_sprite("fingerprints", self.fingerprints)

    def set_emf(self,target_object):
        """Sets the location of an emf point

        Args:
            self (Action_Mode): an instance of Action Mode
            target_object: the name of the object where the emf will be emitted from
        """
        
        emf_x = constants.OBJECT_COORDINATES[target_object][0]
        emf_y = constants.OBJECT_COORDINATES[target_object][1]
        self.emf_position = [emf_x, emf_y]
        print(f'emf set at{emf_x,emf_y}')
        
    def set_freezing(self, target_object):
        """Sets the location of a freezing point

        Args:
            self (Action_Mode): an instance of Action Mode
            target_object: the name of the object where the emf will be emitted from
        """
        pass
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
        pass
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

    def adjust_emf_reading(self,player,timer):
        """Adjusts the EMF reading. It will always be a random value between 0 and 1 unless the player is 150 pixels away from the 
        object that the ghost interacted with. Then the emf reading will be a 5.

        Args:
            self (Action_Mode): an instance of Action Mode
            player (Player): an instance of the player class

        Returns:
            (float) The emf reading to display to the user
        """

        if timer % 30 == 0:
            if self.emf_position == [0,0]:
                self.emf_reading = random.random() + 2
            else:
                x_of_player = player.sprite._get_center_y()
                y_of_player = player.sprite._get_center_y()
                x_of_emf = self.emf_position[0]
                y_of_emf = self.emf_position[1]
                distance = arcade.get_distance(x1=x_of_player, y1=y_of_player, x2=x_of_emf, y2=y_of_emf)
                if distance < 150:
                    self.emf_reading = 5.00
                else: 
                    self.emf_reading = random.random() + 2
            
        return self.emf_reading

    def place_writing(self, book, instruments_list, scene):
        """
        """
        print("writing placed")
        room_coordinates = constants.COORINATE_DICTIONARY[self.room]
        book_x = book._get_center_x()
        book_y = book._get_center_y()

        if book_x in range(room_coordinates[0], room_coordinates [2]):
            if book_y in range(room_coordinates[1], room_coordinates[3]) and self.writing_already == False:
                book.remove_from_sprite_lists()

                book_with_writing = arcade.Sprite(Image_Loader().get_writing(), 1)
                book_with_writing.set_position(book_x, book_y)
                instruments_list[3] = book_with_writing
                scene.add_sprite(constants.INSTRUMENTS[3], instruments_list[3])
                self.writing_already = True


