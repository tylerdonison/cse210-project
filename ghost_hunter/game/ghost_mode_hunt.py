"""This module is in charge of controlling the hunt mode of the ghost"""
import random
import arcade
from pytiled_parser.tiled_object import Point
from game import constants
import math
from game.room import Room

class Hunt_Mode:
    """Class Hunt_Mode allows the ghost to hunt for the player in the room. When in hunt mode ghost can hunt for player 
    """
    def __init__(self, ghost):
        """Class constructor

        Args:
            ghost (Sprite): Ghost will go into hunt_mode to hunt the player.
        """
        # self.target = ghost.target
        # self.ghost = ghost
        # self.sprite = ghost.sprite
        self.ghost_change_x = 0
        self.ghost_change_y = 0

    def hunt(self, wall_list, player, ghost_sprite,time, room_map):

        """Causes the ghost to hunt the player. This means that the ghost moves towards the player
        
        Args:
            wall_list (Sprite): player interacts with walls sprite
            player (Sprite): Player Sprite
            ghost_sprite (Sprite): Ghost sprite
        """
        #physics(player_sprite, front_door_list) #lock front door
        #add sound to indicate locked door
        #generate random coordinates in room
                
        player_position = (player.sprite._get_center_x(), player.sprite._get_center_y())
        ghost_position = (ghost_sprite._get_center_x(), ghost_sprite._get_center_y())

        if time == constants.INTERVAL_BEFORE_HUNT:
            try:
                ghost_position = room_map.generate_random()
                ghost_sprite.set_position(ghost_position)
                print("hunted without errors")
            except:
                ghost_x = random.randint(constants.TOTAL_MAX_COORDINATES[0], constants.TOTAL_MAX_COORDINATES[2])
                ghost_y = random.randint(constants.TOTAL_MAX_COORDINATES[1], constants.TOTAL_MAX_COORDINATES[3])
                ghost_sprite.set_position(ghost_x,ghost_y)
                print("sweeping errors under the rug again...")
            

        if time > constants.INTERVAL_BEFORE_HUNT * 60:
            if arcade.has_line_of_sight(player_position, ghost_position, wall_list):
                self.follow_sprite(player, ghost_sprite)
            else:
                self.random_search(ghost_sprite)

        
    def hunt_check(self, sanity):
        """Checks to see if the ghost will hunt the player. There is a 1 in 20 chance of being hunted if they have 100 sanity
        and a 1 in 1 chance if their sanity gets to 5

        Args:
            sanity (int): The ammount of sanity that the player has.

        """
        #This ensures that the chance of being hunted will never be greater than a 1 in 1 chance (prevent bugs)
        if sanity < 5:
            sanity = 5 #Remember that this won't change sanity globally. Just don't pass in sanity as a number instead of accessing it through an object

        chance_of_being_hunted_inverse = int(sanity / 4)
        round(chance_of_being_hunted_inverse) #ensures that the chance of being hunted will be an int

        #creates a list from 1 to the inverse of the chance of being hunted. (A greater number is better for the player). Then randomly chooses a number
        #from the list. If it is a one, they will be hunted. Chances of having a 1 increase with a smaller list.
        chance_list = []
        for i in range(chance_of_being_hunted_inverse):
            chance_list.append(i + 1)

        random_number_in_chance_list = random.choice(chance_list)
        if random_number_in_chance_list == 1:
            ghost_hunt_mode = True
        else:
            ghost_hunt_mode = False
        return ghost_hunt_mode #This will probably need to be changed to an object that is passed in

    def follow_sprite(self, player_sprite, ghost):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        
        Args:
            player_sprite (Sprite): Player Sprite
            ghost (Sprite): Ghost Sprite
        """
        # Random 1 in 100 chance that we'll change from our old direction and
        # then re-aim toward the player
        ghost.center_x += self.ghost_change_x
        ghost.center_y += self.ghost_change_y
        
        if random.randrange(2) == 0:
            start_x = ghost.center_x
            start_y = ghost.center_y

            # Get the destination location for the Ghost
            dest_x = player_sprite.sprite.center_x
            dest_y = player_sprite.sprite.center_y

            # Do math to calculate how to get the Ghost to the destination.
            # Calculate the angle in radians between the start points
            # and end points. This is the angle the Ghost will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the Ghost travels.
            self.ghost_change_x = math.cos(angle) * constants.GHOST_MOVEMENT_SPEED
            self.ghost_change_y = math.sin(angle) * constants.GHOST_MOVEMENT_SPEED    

    def random_search(self,ghost):
        """
        This function will move the current sprite towards whatever
        other sprite is specified as a parameter.

        We use the 'min' function here to get the sprite to line up with
        the target sprite, and not jump around if the sprite is not off
        an exact multiple of SPRITE_SPEED.
        """


        ghost.center_x += self.ghost_change_x
        ghost.center_y += self.ghost_change_y
        
        ghost_turn_probability = 240 #higher should take the ghost longer to turn. This should be every 4 seconds now
        if random.randrange(ghost_turn_probability) == 0:
            start_x = ghost.center_x
            start_y = ghost.center_y

            # Get the destination location for the Ghost
            dest_x = random.randint(constants.TOTAL_MAX_COORDINATES[0], constants.TOTAL_MAX_COORDINATES[2])
            dest_y = random.randint(constants.TOTAL_MAX_COORDINATES[1], constants.TOTAL_MAX_COORDINATES[3])

            # Do math to calculate how to get the Ghost to the destination.
            # Calculate the angle in radians between the start points
            # and end points. This is the angle the Ghost will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Taking into account the angle, calculate our change_x
            # and change_y. Velocity is how fast the Ghost travels.
            self.ghost_change_x = math.cos(angle) * constants.GHOST_MOVEMENT_SPEED
            self.ghost_change_y = math.sin(angle) * constants.GHOST_MOVEMENT_SPEED 
