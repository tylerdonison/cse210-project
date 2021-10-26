"""This is the module in charge of controlling the ghost
"""
from game.image_loader import Image_Loader
import math
import random
import arcade
from game.ghost_mode_action import Action_Mode
from game.ghost_mode_hunt import Hunt_Mode
import os
from game import constants

#constants
GHOST_SPEED = 0.5
SPRITE_SPEED = 0.5

class Ghost(arcade.Sprite):
    """The ghost is a spooky being who leaves clues and hunts the player.

    Stereotype: Information Holder, Controller

    Attributes:
        cooldown_time (int): The cooldown time for hunt mode.
        hunt_time (int): The duration of the hunt.
        time_since_last_interaction (int): The time that passed since the last interaction.
        hunt_mode_on (boolean): Whether the ghost is hunting or not.
        hunt_mode (Hunt_Mode): A Hunt_Mode object to control the hunt mode of the ghost.
        action_mode (Action_Mode): A Action_Mode object to control the action mode of the ghost.
        hunt_duration (int): The duration of a hunt
        max_cooldown_time (int): The maximum a cooldown can last. 
    """
    def __init__(self, player, room, book):
        """The class constructor

        Args:
            self (Ghost): An instance of Ghost
            player: The player sprite
            Room:
            Book: The book sprite
        """

        super().__init__()

        main_image = Image_Loader().ghost_front_path

        self.sprite = arcade.Sprite(main_image, .75)
        self.sprite._set_center_x(1856)
        self.sprite._set_center_y(64)

       
        self.cooldown_time = 0
        self.hunt_time = 0
        self.timer = 0
        self.hunt_mode_on = False
        self.ghost_type = random.choice(constants.GHOST_TYPES)    
        self.action_mode = Action_Mode(self.ghost_type, room)
        self.hunt_duration = constants.HUNT_DURATION * 60

        self.max_cooldown_time = constants.MAX_COOLDOWN_TIME * 60

        self.target = player
        self.book = book
        self.hunt_mode = Hunt_Mode()
        self.time_between_probability = constants.TIME_BETWEEN_PROBABILITES * 60 #time between checking to see if the ghost will hunt, do an action, or nothing
        self.heart_beat = self.hunt_mode.heart_beat

    def execute(self,sanity,scene, wall_list, room, instruments_list):

        """This executes all of the updates and actions that the ghost object should have during
        each cycle.

        Args: 
            self (Ghost): An instance of Ghost
            sanity (int): the players current sanity
            wall_list(list): the wall list
        """

        self.update_time_and_status(sanity,scene, room, instruments_list)
        self.do_hunt(wall_list,room)
        #temp_reading = self.action_mode.adjust_temp_reading()
        return (self.action_mode.adjust_emf_reading(self.target, self.timer)) 

    def update_time_and_status(self,sanity,scene, room, instruments_list):
        """This method updates the cooldown time or, if the ghost is hunging, the hunt time.

        Args: 
            self (Ghost): An instance of Ghost
            sanity (int): the player's current sanity
            scene (obj): The scene object
        """
        self.timer += 1
        if self.hunt_mode_on == True:
            self.hunt_time += 1
            self.cooldown_time = 0

            if self.hunt_time > self.hunt_duration:
                self.hunt_mode_on = False
                self.hunt_time = 0
                self.sprite.set_position(1856,320)     
        else:
            self.cooldown_time +=1
            self.choose_ghost_action(sanity,scene, instruments_list)


    def choose_ghost_action(self,sanity,scene, instruments_list):
        """This method causes the ghost to do one of three things. There is a 50 percent chance that it will
        cause a hunt check, a 10 percent chance it will do nothing, and a 40 percent chance that it will leave 
        a clue. The ghost will not hunt if the cooldown timer has not expired. This method should not be executed 
        while the ghost is in hunt mode.
        Args:
            self (Ghost): An instance of Ghost                    
            sanity (int): the player's current sanity
            scene (obj): the scene object
        """
        probability = [1,2,3,4,5,6,7,8,9,10]
        if (self.timer) % self.time_between_probability == 0:
            random_decision = random.choice(probability)
            if (random_decision < 7) and (self.cooldown_time > self.max_cooldown_time) and (sanity < constants.MAX_SANITY_BEFORE_HUNT):
                self.hunt_mode_on = self.hunt_mode.hunt_check(sanity)
                self.timer = 0
            elif (random_decision > 7):
                self.action_mode.cause_ghost_interaction(scene,self.book, instruments_list)
        
    def do_hunt(self, wall_list, room):
        """If hunt_mode is active, this will cause the ghost to hunt the player.

        Args:
            self (Ghost): An instance of Ghost
        """
        if self.hunt_mode_on == True:
            self.heart_beat = self.hunt_mode.hunt(wall_list, self.target, self.sprite,self.hunt_time, room)            

    def check_correct_instrument(self, instrument):
        """
        Checks if the given instrument index is the correct one for catching the ghost
        
        Returns:
            bool: true
        """
        return True

