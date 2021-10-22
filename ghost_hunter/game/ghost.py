"""This is the module in charge of controlling the ghost
"""
from game.image_loader import Image_Loader
import math
import random
import arcade
from game.ghost_mode_action import Action_Mode
from game.ghost_mode_hunt import Hunt_Mode
import os
from game.constants import CHARACTER_SCALING
from game.entity import Entity

#constants
GHOST_SPEED = 0.5
SPRITE_SPEED = 0.5

class Ghost(Entity):
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
    def __init__(self, player, room):
        """The class constructor

        Args:
            self (Ghost): An instance of Ghost
        """
        Entity.__init__(self)
        self.path = Image_Loader().ghost_front_path
        self.sprite = arcade.Sprite(self.path, CHARACTER_SCALING)
        Entity.setup(
            self, self.path, 1856, 64)


        # self.room = room
        self.cooldown_time = 0
        self.hunt_time = 0
        self.timer = 0
        self.hunt_mode_on = False

        self.action_mode = Action_Mode("poltergeist", room)
        self.hunt_duration = 15 * 60

        self.max_cooldown_time = 30 * 60
        self.ghost_type = "poltergeist"
        self.target = player
        self.hunt_mode = Hunt_Mode(self)


    def execute(self,sanity,scene, wall_list, room):

        """This executes all of the updates and actions that the ghost object should have during
        each cycle.

        Args: 
            self (Ghost): An instance of Ghost
            sanity (int): the players current sanity
            wall_list(list): the wall list
        """

        self.update_time_and_status(sanity,scene, room)
        self.do_hunt(wall_list)

        #emf_reading = self.action_mode.adjust_emf_reading()
        #temp_reading = self.action_mode.adjust_temp_reading()

    def update_time_and_status(self,sanity,scene, room):
        """This method updates the cooldown time or, if the ghost is hunging, the hunt time.

        Args: 
            self (Ghost): An instance of Ghost
            sanity (int): the player's current sanity
            scene (obj): The scene object
        """
        if self.hunt_mode_on == True:
            self.hunt_time += 1
            self.cooldown_time = 0

            if self.hunt_time > self.hunt_duration:
                self.hunt_mode_on = False
                self.hunt_time = 0
                self.choose_ghost_action(sanity, scene, room)
        else:
            self.cooldown_time +=1
            self.choose_ghost_action(sanity,scene, room)
            #self.sprite.set_position(1856, 320)


    def choose_ghost_action(self,sanity,scene, room):
        """This method causes the ghost to do one of three things. There is a 20 percent chance that it will
        cause a hunt check, a 40 percent chance it will do nothing, and a 40 percent chance that it will leave 
        a clue. This method is executed every 10 seconds. The ghost will not hunt if the cooldown timer has not
        expired. This method should not be executed while the ghost is in hunt mode.
        Args:
            self (Ghost): An instance of Ghost                    
            sanity (int): the player's current sanity
            scene (obj): the scene object
        """
        self.timer += 1 
        probability = [1,2,3,4,5,6,7,8,9,10]

        if (self.timer) % 10 == 0:
            random_decision = random.choice(probability)
            if (random_decision < 3) and (self.cooldown_time > self.max_cooldown_time) and (sanity < 51):
                self.hunt_mode_on = self.hunt_mode.hunt_check(sanity, room, self.sprite)
            elif (random_decision > 6):
                self.action_mode.cause_ghost_interaction(self.ghost_type,scene)
        
    def do_hunt(self, wall_list):
        """If hunt_mode is active, this will cause the ghost to hunt the player.

        Args:
            self (Ghost): An instance of Ghost
        """
        if self.hunt_mode_on == True:
            self.hunt_mode.hunt(wall_list, self.target, self.sprite,self.hunt_time)


    def check_correct_instrument(self, instrument):
        """
        Checks if the given instrument index is the correct one for catching the ghost
        
        Returns:
            bool: true
        """
        return True

